from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Person, Movie


def index(request):
    return HttpResponse('home_page')


class PersonList(ListView):
    model = Person


class PersonDetail(DetailView):
    model = Person


class MovieList(ListView):
    model = Movie


class MovieDetail(DetailView):
    slug_field = 'translations__slug'
    model = Movie
