from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _

from . import views

urlpatterns = patterns('',
    url(
        r'^$',
        views.index,
        name='home_page'
    ),
)

urlpatterns += patterns('',
    url(
        _(r'^persons/$'),
        views.PersonList.as_view(),
        name='person_list'
    ),
    url(
        _(r'^persons/(?P<slug>[-\w]+)/$'),
        views.PersonDetail.as_view(),
        name='person_detail'
    ),
)

urlpatterns += patterns('',
    url(
        _(r'^movies/$'),
        views.MovieList.as_view(),
        name='movie_list'
    ),
    url(
        _(r'^movies/(?P<slug>[-\w]+)/$'),
        views.MovieDetail.as_view(),
        name='movie_detail'
    ),
)
