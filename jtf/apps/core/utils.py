# -*- coding: utf-8 -*-
import os

from django.conf import settings

def get_media_directory(filename):
    directory = os.path.join(filename[:2], filename[2:4])
    absolute_directory = os.path.join(settings.MEDIA_ROOT, directory)
    if not os.path.exists(absolute_directory):
        os.makedirs(absolute_directory)
    return directory
