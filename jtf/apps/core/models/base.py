from django.db import models

from polymorphic import PolymorphicModel


class MovieObject(models.Model):
    imdb_id = models.CharField('IMDB ID', max_length=12, null=True,
                               blank=True, unique=True)
    tmdb_id = models.CharField('TMDB ID', max_length=12, null=True,
                               blank=True, unique=True)

    class Meta:
        abstract = True
