from django.conf import settings
from django.conf.urls import patterns, include, url

from jtf.urls import urlpatterns

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
