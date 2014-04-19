from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _

from polymorphic import PolymorphicModel
from django_extensions.db.models import TimeStampedModel


class Media(PolymorphicModel, TimeStampedModel):
    title = models.CharField(_('title'), max_length=100)
    file = models.FileField(upload_to='files')
    description = models.TextField(_('description'), blank=True)
    created_by = models.ForeignKey(
        getattr(settings, 'AUTH_USER_MODEL', 'auth.User'),
        related_name='owned_%(class)ss',
        null=True, blank=True, verbose_name=_('owner')
    )

    class Meta:
        app_label = 'media'

    def preview(self):
        raise NotImplementedError

