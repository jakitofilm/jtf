from django.db import models
from parler.managers import TranslatableManager


class PersonManager(models.Manager):
    def actors(self, **kwargs):
        return self.filter(is_actor=True, **kwargs)

    def directors(self, **kwargs):
        return self.filter(is_director=True, **kwargs)

    def writers(self, **kwargs):
        return self.filter(is_writer=True, **kwargs)

    def producers(self, **kwargs):
        return self.filter(is_producer=True, **kwargs)


class MovieManager(TranslatableManager):
    pass
