# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Movie.cover'
        db.add_column(u'core_movie', 'cover',
                      self.gf('django.db.models.fields.related.OneToOneField')(related_name='movie', unique=True, null=True, to=orm['core.Image']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Movie.cover'
        db.delete_column(u'core_movie', 'cover_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.cast': {
            'Meta': {'object_name': 'Cast'},
            'actor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'roles'", 'to': "orm['core.Person']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cast'", 'to': "orm['core.Movie']"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '-1'})
        },
        'core.casttranslation': {
            'Meta': {'unique_together': "[(u'language_code', u'master')]", 'object_name': 'CastTranslation', 'db_table': "u'core_cast_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            u'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['core.Cast']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.image': {
            'Meta': {'object_name': 'Image', '_ormbases': ['core.MediaObject']},
            'file': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            u'mediaobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.MediaObject']", 'unique': 'True', 'primary_key': 'True'})
        },
        'core.mediaobject': {
            'Meta': {'object_name': 'MediaObject'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_mediaobjects'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_core.mediaobject_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'core.movie': {
            'Meta': {'object_name': 'Movie'},
            'actors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'appeared_in_movies'", 'symmetrical': 'False', 'through': "orm['core.Cast']", 'to': "orm['core.Person']"}),
            'cover': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'movie'", 'unique': 'True', 'null': 'True', 'to': "orm['core.Image']"}),
            'directors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'directed_movies'", 'symmetrical': 'False', 'to': "orm['core.Person']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imdb_id': ('django.db.models.fields.CharField', [], {'max_length': '12', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'tmdb_id': ('django.db.models.fields.CharField', [], {'max_length': '12', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'core.movietranslation': {
            'Meta': {'unique_together': "[(u'language_code', u'master')]", 'object_name': 'MovieTranslation', 'db_table': "u'core_movie_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            u'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['core.Movie']"}),
            'slug': ('jtf.apps.core.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "['title']", 'overwrite': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.person': {
            'Meta': {'ordering': "('last_name',)", 'object_name': 'Person'},
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'deathday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imdb_id': ('django.db.models.fields.CharField', [], {'max_length': '12', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'is_actor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_director': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_producer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_writer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'place_of_birth': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'slug': ('jtf.apps.core.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "['first_name', 'last_name']", 'overwrite': 'False'}),
            'tmdb_id': ('django.db.models.fields.CharField', [], {'max_length': '12', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']