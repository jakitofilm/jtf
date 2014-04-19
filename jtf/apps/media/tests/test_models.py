# -*- coding: utf-8 -*-
from django.test import TestCase

from ..models import Media, Image


class TestMedia(TestCase):

    def test_media_preview(self):
        media = Media.objects.create(title=u'Test mediów')

        media.preview()


class TestImage(TestCase):

    def test_image_preview(self):
        media = Image.objects.create(title=u'Test mediów')

        media.preview()
