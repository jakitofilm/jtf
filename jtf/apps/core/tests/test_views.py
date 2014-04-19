from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from . import PersonTestMixin, MovieTestMixin


class PersonViewTest(PersonTestMixin, TestCase):

    def setUp(self):
        self.client = Client()
        super(PersonViewTest, self).setUp()

    def test_person_list(self):
        response = self.client.get(reverse('core:person_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 4)

    def test_person_list_url(self):
        response = self.client.get(reverse('core:person_list'))
        self.assertIn(self.nicolas.get_absolute_url(), response.content)
        self.assertIn(self.jonathan.get_absolute_url(), response.content)
        self.assertIn(self.copola.get_absolute_url(), response.content)

    def test_person_detail(self):
        response = self.client.get(self.nicolas.get_absolute_url())
        nicolas = response.context['object']
        self.assertIn('<h1>%s</h1>' % nicolas.fullname, response.content)
        self.assertEqual(response.status_code, 200)


class MovieViewTest(MovieTestMixin, TestCase):

    def setUp(self):
        self.client = Client()
        super(MovieViewTest, self).setUp()

    def test_movie_list(self):
        response = self.client.get(reverse('core:movie_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 1)
        self.assertIn('Szyfry wojny', response.content)

    def test_movie_detail(self):
        self.windtalkers.set_current_language('pl')
        response = self.client.get(
            reverse('core:movie_detail', args=('szyfry-wojny',))
        )
        windtalkers = response.context['object']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.windtalkers, windtalkers)
        self.assertIn('<h1>%s</h1>' % self.windtalkers.title, response.content)

        for role in self.windtalkers.cast.all():
            self.assertIn(
                '<a href="{0}">{1}</a>'.format(role.actor.get_absolute_url(), role.actor), response.content
            )

    # def test_movie_list_url(self):
    #     response = self.client.get(reverse('core:person_list'))
    #     self.assertIn(self.nicolas.get_absolute_url(), response.content)
    #     self.assertIn(self.jonathan.get_absolute_url(), response.content)
    #     self.assertIn(self.copola.get_absolute_url(), response.content)

    # def test_person_detail(self):
    #     response = self.client.get(self.nicolas.get_absolute_url())
    #     nicolas = response.context['object']
    #     self.assertIn('<h1>%s</h1>' % nicolas.fullname, response.content)
    #     self.assertEqual(response.status_code, 200)
