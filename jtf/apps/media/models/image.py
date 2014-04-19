from django.db import models
from django.utils.translation import ugettext as _

from sorl.thumbnail import ImageField

from .base import Media


class Image(Media):
    def __init__(self, *args, **kwargs):
        super(Image, self).__init__(*args, **kwargs)
        self.file = ImageField(upload_to='images')

    class Meta:
        app_label = 'media'

    def preview(self):
        raise NotImplementedError

