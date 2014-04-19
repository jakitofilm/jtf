from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _

from .base import MovieObject
from .managers import PersonManager
from jtf.apps.core.fields import PolishAutoSlugField


class Person(MovieObject):
    first_name = models.CharField(_('first name'), max_length=100)
    last_name = models.CharField(_('last name'), max_length=100)
    slug = PolishAutoSlugField(populate_from=['first_name', 'last_name'])
    birthday = models.DateField(_('birth day'), blank=True, null=True)
    deathday = models.DateField(_('death day'), blank=True, null=True)
    place_of_birth = models.CharField(_('place of birth'), max_length=250,
                                      blank=True)
    is_actor = models.BooleanField(_('is actor'), default=False)
    is_director = models.BooleanField(_('is director'), default=False)
    is_writer = models.BooleanField(_('is writer'), default=False)
    is_producer = models.BooleanField(_('is producer'), default=False)

    objects = PersonManager()

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('people')
        ordering = ('last_name',)
        app_label = 'core'

    def __unicode__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse('core:person_detail', args=(self.slug,))

    @property
    def fullname(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
