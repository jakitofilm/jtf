import os
import urllib2
import hashlib

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.db import models
from django.utils.translation import ugettext as _

from sorl.thumbnail import ImageField

from .base import MediaObject
from jtf.apps.core.utils import get_media_directory


def movie_images(instance, filename):
    hash_filename = hashlib.md5(filename).hexdigest()
    new_filename = '%s%s' % (hash_filename, filename[filename.rfind('.'):])
    path = os.path.join(get_media_directory(hash_filename), new_filename)
    return path


class Image(MediaObject):
    file = ImageField(upload_to=movie_images)

    class Meta:
        app_label = 'core'
        verbose_name = _('image')
        verbose_name_plural = _('images')

    def preview(self):
        raise NotImplementedError

    @classmethod
    def fetch_from_url(cls, url):
        ext = url[url.rfind('.'):]
        im = cls._default_manager.create()
        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(urllib2.urlopen(url).read())
        img_temp.flush()
        im.file.save('%s.%s' % (img_temp.name, ext), File(img_temp))
        return im

