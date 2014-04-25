# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _

from parler.models import TranslatableModel, TranslatedFields
from parler.utils.context import smart_override
from positions import PositionField

from .base import MovieObject
from .media import Image
from .person import Person
from .managers import MovieManager
from jtf.apps.core.fields import PolishAutoSlugField
from jtf.apps.core.api_worker.decorators import fetch_from_api_worker


class Movie(TranslatableModel, MovieObject):
    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=100),
        slug=PolishAutoSlugField(populate_from=['title']),
    )
    cover = models.OneToOneField(Image, null=True, related_name='movie')
    year = models.PositiveSmallIntegerField(_('year'), blank=True, default=0)
    directors = models.ManyToManyField(Person, related_name='directed_movies')
    actors = models.ManyToManyField(
        Person, related_name='appeared_in_movies',
        through='Cast'
    )
    objects = MovieManager()

    class Meta:
        app_label = 'core'
        verbose_name = _('movie')
        verbose_name_plural = _('movies')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.slug})

    @property
    def titles(self):
        return {obj.language_code: obj.title
                for obj in self.translations.all()}

    @classmethod
    @fetch_from_api_worker('imdb/movie/{0}')
    def create_from_imdb(cls, imdb_id):
        with smart_override('en'):
            movie, _ = cls._default_manager.get_or_create(imdb_id=imdb_id)
            movie.title = api_result['title']
            movie.year = api_result['year']
            movie.cover = Image.fetch_from_url(api_result['cover'])

        for lang, title in api_result['akas'].iteritems():
            movie.set_current_language(lang)
            movie.title = title
        movie.save()

        for person in api_result['director']:
            director, _ = Person.objects.get_or_create(**person)
            director.is_director = True
            director.save()
            movie.directors.add(director)

        for pos, cast in enumerate(api_result['cast']):
            role = cast.pop('role', u'')
            actor, _ = Person.objects.get_or_create(**cast)
            actor.is_actor = True
            Cast.objects.create(order=pos, actor=actor, movie=movie, role=role)

        movie.save()
        return movie


class Cast(TranslatableModel):
    movie = models.ForeignKey('Movie', related_name='cast')
    actor = models.ForeignKey(Person, related_name='roles')
    order = PositionField(collection='actor')
    translations = TranslatedFields(
        role=models.CharField(_('as'), max_length=100)
    )

    class Meta:
        app_label = 'core'
        verbose_name = _('cast')
        verbose_name_plural = _('cast')

    def __unicode__(self):
        return u'{0} in {1}'.format(self.actor, self.movie)
