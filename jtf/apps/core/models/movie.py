# -*- coding: utf-8 -*-
import requests
import json

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _

from parler.models import TranslatableModel, TranslatedFields
from parler.utils.context import smart_override
from positions import PositionField

from .base import MovieObject
from .person import Person
from .managers import MovieManager
from jtf.apps.core.fields import PolishAutoSlugField
from jtf.apps.core.api_worker.decorators import fetch_from_api_worker


class Movie(TranslatableModel, MovieObject):
    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=100),
        slug=PolishAutoSlugField(populate_from=['title'])
    )
    year = models.PositiveSmallIntegerField(_('year'))
    directors = models.ManyToManyField(Person, related_name='directed_movies')
    actors = models.ManyToManyField(
        Person, related_name='appeared_in_movies',
        through='Cast'
    )
    objects = MovieManager()

    class Meta:
        app_label = 'core'

    def __unicode__(self):
        return self.title

    @property
    def titles(self):
        return {obj.language_code: obj.title
                for obj in self.translations.all()}

    @classmethod
    @fetch_from_api_worker('imdb/movie/{0}')
    def create_from_imdb(cls, imdb_id):
        with smart_override('en'):
            movie = cls._default_manager.create(
                title=api_result['title'], year=api_result['year'])

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

    def __unicode__(self):
        return u'{0} in {1}'.format(self.actor, self.movie)
