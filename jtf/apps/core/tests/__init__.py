# -*- coding: utf-8 -*-
from datetime import date
import factory

from .. import models


class PersonFactory(factory.Factory):
    FACTORY_FOR = models.Person

    birthday = date(year=2010, month=6, day=22)
    place_of_birth = 'test'
    is_writer = False
    is_producer = False
    is_actor = False
    is_director = False


class MovieFactory(factory.Factory):
    FACTORY_FOR = models.Movie


class PersonTestMixin(object):
    def setUp(self):
        super(PersonTestMixin, self).setUp()
        self.nicolas = PersonFactory.create(
            tmdb_id='0000115', imdb_id='2963',
            first_name='Nicolas', last_name='Cage',
            is_actor=True, is_producer=True
        )
        self.jonathan = PersonFactory.create(
            tmdb_id='0634300', imdb_id='527',
            first_name='Jonathan', last_name='Nolan',
            is_writer=True, is_producer=True
        )

        self.copola = PersonFactory.create(
            tmdb_id='0000338', imdb_id='1776',
            first_name='Francis', last_name='Ford Copola',
            is_director=True
        )
        self.woo = PersonFactory.create(
            tmdb_id='0000247', imdb_id='11401',
            first_name='John', last_name='Woo',
            is_director=True, is_writer=True
        )

        self.nicolas.save()
        self.jonathan.save()
        self.copola.save()
        self.woo.save()


class MovieTestMixin(PersonTestMixin):
    def setUp(self):
        super(MovieTestMixin, self).setUp()
        self.windtalkers = MovieFactory.create(
            imdb_id='0245562', tmdb_id='12100',
            title='Szyfry wojny', year=2002
        )
        self.windtalkers.set_current_language('en')
        self.windtalkers.title = 'Windtalkers'
        self.windtalkers.save()

        self.windtalkers.directors.add(self.woo)

        role = models.Cast(
            movie=self.windtalkers, actor=self.nicolas,
            role=u'Sierżant Joe Enders'
        )
        role.set_current_language('en')
        role.role = 'Sergeant Joe Enders'
        role.save()

        self.windtalkers.save()
