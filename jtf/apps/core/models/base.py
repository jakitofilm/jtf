from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _

from polymorphic import PolymorphicModel


class MovieObject(models.Model):
    imdb_id = models.CharField('IMDB ID', max_length=12, null=True,
                               blank=True, unique=True)
    tmdb_id = models.CharField('TMDB ID', max_length=12, null=True,
                               blank=True, unique=True)

    class Meta:
        abstract = True


class MediaObject(PolymorphicModel):
    title = models.CharField(_('title'), max_length=100, blank=True)
    _type = 'object'

    owner = models.ForeignKey(
        getattr(settings, 'AUTH_USER_MODEL', 'auth.User'),
        related_name='owned_%(class)ss',
        null=True, blank=True, verbose_name=_('owner')
    )

    created = models.DateTimeField(_('uploaded at'), auto_now_add=True)
    modified = models.DateTimeField(_('modified at'), auto_now=True)

    class Meta:
        app_label = 'core'
