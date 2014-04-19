#! -*- coding: utf-8 -*-
from django.template import defaultfilters

from django_extensions.db.fields import AutoSlugField
from unidecode import unidecode


class PolishAutoSlugField(AutoSlugField):
    """
    Convert national char to euvalent in neutral language.
    E.g.: ą -> a
    """
    def slugify_func(self, content):
        if content:
            return defaultfilters.slugify(unidecode(unicode(content)))
        return ''
