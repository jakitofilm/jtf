# -*- coding: utf-8 -*-
from django.test import TestCase

from parler.utils.context import smart_override, switch_language

from . import PersonTestMixin, MovieTestMixin
from ..models import Person, Movie, Image


class TestPerson(PersonTestMixin, TestCase):

    def test_first_name(self):
        self.assertEquals(self.nicolas.first_name, u'Nicolas')
        self.assertEquals(self.jonathan.first_name, u'Jonathan')
        self.assertEquals(self.copola.first_name, u'Francis')

    def test_last_name(self):
        self.assertEquals(self.nicolas.last_name, u'Cage')
        self.assertEquals(self.jonathan.last_name, u'Nolan')
        self.assertEquals(self.copola.last_name, u'Ford Copola')

    def test_unicode(self):
        self.assertEquals(unicode(self.nicolas), u'Nicolas Cage')
        self.assertEquals(unicode(self.jonathan), u'Jonathan Nolan')
        self.assertEquals(unicode(self.copola), u'Francis Ford Copola')

    def test_manager_get_actors(self):
        self.assertIn(self.nicolas, Person.objects.actors())

    def test_manager_get_directors(self):
        self.assertIn(self.copola, Person.objects.directors())

    def test_manager_get_writers(self):
        self.assertIn(self.jonathan, Person.objects.writers())

    def test_manager_get_producers(self):
        self.assertIn(self.jonathan, Person.objects.producers())

    def test_nicolas_absolute_url(self):
        self.assertEquals(self.nicolas.get_absolute_url(),
                          '/persons/nicolas-cage/')


class TestMovie(MovieTestMixin, TestCase):

    def test_multilanguage_title(self):
        with switch_language(self.windtalkers, 'pl'):
            self.assertEqual(self.windtalkers.title, 'Szyfry wojny')
        with switch_language(self.windtalkers, 'en'):
            self.assertEqual(self.windtalkers.title, 'Windtalkers')

    def test_director(self):
        self.assertIn(self.woo, self.windtalkers.directors.all())

    def test_actors(self):
        self.assertIn(self.nicolas, self.windtalkers.actors.all())

    def test_cast_multilanguage(self):
        cast = self.windtalkers.cast
        nicolas = cast.all()[0]
        with switch_language(nicolas, 'pl'):
            self.assertEqual(nicolas.role, u'Sierżant Joe Enders')
        with switch_language(nicolas, 'en'):
            self.assertEqual(nicolas.role, u'Sergeant Joe Enders')

    def test_get_titles(self):
        titles = self.windtalkers.titles
        self.assertEqual(len(titles), 2)
        self.assertDictEqual(
            titles, {'pl': u'Szyfry wojny', 'en': u'Windtalkers'}
        )


class FetchFromApi(TestCase):

    def test_fetch_from_imdb(self):
        movie = Movie.create_from_imdb('0245562')
        with switch_language(movie, 'en'):
            self.assertEqual(movie.title, u'Windtalkers')
        self.assertEqual(movie.year, 2002)

        self.assertDictEqual(
            movie.titles, {u'de': u'Windtalkers',
                           u'en': u'Windtalkers',
                           u'es': u'Windtalkers',
                           u'fr': u'Windtalkers - Les messagers du vent',
                           u'it': u'Windtalkers',
                           u'pl': u'Szyfry wojny'}
        )

        self.assertEqual(movie.cast.count(), 74)

        self.assertEqual(movie.directors.count(), 1)
        self.assertEqual(movie.directors.all()[0].fullname, u'John Woo')

        with switch_language(movie, 'en'):
            self.assertTrue(movie.cover)


class ImageMedia(TestCase):

    def test_fetch_from_url(self):
        const_url = 'http://lorempixel.com/400/200/sports/'
        image = Image.fetch_from_url(const_url)
        # self.assertEqual(len(image.file), 2163)
