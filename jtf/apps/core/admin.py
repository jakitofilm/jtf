from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from django.utils.translation import ugettext_lazy as _

from parler.admin import TranslatableAdmin

from .models import Person, Movie, Cast


class PersonAdmin(admin.ModelAdmin):
    suit_form_tabs = (
        (_('general'), _('IDs')),
        (_('basic'), _('Basic information'))
    )
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('tmdb_id', 'imdb_id'),
        }),
        ("Basic information", {
            'classes': ('suit-tab suit-tab-basic',),
            'fields': ('first_name', 'last_name',),
        }),
        ("Dates", {
            'classes': ('suit-tab suit-tab-basic',),
            'fields': ('birthday', 'place_of_birth', 'deathday'),
        }),
        ("Job", {
            'classes': ('suit-tab suit-tab-basic',),
            'fields': ('is_actor', 'is_director', 'is_writer', 'is_producer',)
        })
    )
admin.site.register(Person, PersonAdmin)


class MovieAdmin(TranslatableAdmin):
    suit_form_tabs = (
        (_('general'), _('Titles')),
        (_('basic'), _('Basic information')),
        (_('cast'), _('Cast')),
    )
    list_display = ('title', 'year', 'language_column')
    list_filter = ('year',)
    raw_id_fields = ['directors', 'actors']
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('title',),
        }),
        ("Contents", {
            'classes': ('suit-tab suit-tab-basic',),
            'fields': ('imdb_id', 'tmdb_id', 'year',),
        })
    )
admin.site.register(Movie, MovieAdmin)


class CastAdmin(TranslatableAdmin):
    list_display = ('role', 'movie', 'actor')
    raw_id_fields = ['movie', 'actor']
    suit_form_tabs = (
        (_('general'), _('Role')),
    )
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('role',),
        }),
        ("Person", {
            'fields': ('actor', 'movie'),
        })

    )
admin.site.register(Cast, CastAdmin)
