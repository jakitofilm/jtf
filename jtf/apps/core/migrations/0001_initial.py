# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MediaObject'
        db.create_table(u'core_mediaobject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name='polymorphic_core.mediaobject_set', null=True, to=orm['contenttypes.ContentType'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='owned_mediaobjects', null=True, to=orm['auth.User'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('core', ['MediaObject'])

        # Adding model 'Image'
        db.create_table(u'core_image', (
            (u'mediaobject_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.MediaObject'], unique=True, primary_key=True)),
            ('file', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Image'])

        # Adding model 'Person'
        db.create_table(u'core_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imdb_id', self.gf('django.db.models.fields.CharField')(max_length=12, unique=True, null=True, blank=True)),
            ('tmdb_id', self.gf('django.db.models.fields.CharField')(max_length=12, unique=True, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('jtf.apps.core.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from=['first_name', 'last_name'], overwrite=False)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('deathday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('place_of_birth', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('is_actor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_director', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_writer', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_producer', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('core', ['Person'])

        # Adding model 'MovieTranslation'
        db.create_table(u'core_movie_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('cover', self.gf('django.db.models.fields.related.ForeignKey')(related_name='movie', null=True, to=orm['core.Image'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('jtf.apps.core.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from=['title'], overwrite=False)),
            (u'master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['core.Movie'])),
        ))
        db.send_create_signal('core', ['MovieTranslation'])

        # Adding unique constraint on 'MovieTranslation', fields ['language_code', u'master']
        db.create_unique(u'core_movie_translation', ['language_code', u'master_id'])

        # Adding model 'Movie'
        db.create_table(u'core_movie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imdb_id', self.gf('django.db.models.fields.CharField')(max_length=12, unique=True, null=True, blank=True)),
            ('tmdb_id', self.gf('django.db.models.fields.CharField')(max_length=12, unique=True, null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('core', ['Movie'])

        # Adding M2M table for field directors on 'Movie'
        m2m_table_name = db.shorten_name(u'core_movie_directors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm['core.movie'], null=False)),
            ('person', models.ForeignKey(orm['core.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movie_id', 'person_id'])

        # Adding model 'CastTranslation'
        db.create_table(u'core_cast_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['core.Cast'])),
        ))
        db.send_create_signal('core', ['CastTranslation'])

        # Adding unique constraint on 'CastTranslation', fields ['language_code', u'master']
        db.create_unique(u'core_cast_translation', ['language_code', u'master_id'])

        # Adding model 'Cast'
        db.create_table(u'core_cast', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cast', to=orm['core.Movie'])),
            ('actor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='roles', to=orm['core.Person'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=-1)),
        ))
        db.send_create_signal('core', ['Cast'])


    def backwards(self, orm):
        # Removing unique constraint on 'CastTranslation', fields ['language_code', u'master']
        db.delete_unique(u'core_cast_translation', ['language_code', u'master_id'])

        # Removing unique constraint on 'MovieTranslation', fields ['language_code', u'master']
        db.delete_unique(u'core_movie_translation', ['language_code', u'master_id'])

        # Deleting model 'MediaObject'
        db.delete_table(u'core_mediaobject')

        # Deleting model 'Image'
        db.delete_table(u'core_image')

        # Deleting model 'Person'
        db.delete_table(u'core_person')

        # Deleting model 'MovieTranslation'
        db.delete_table(u'core_movie_translation')

        # Deleting model 'Movie'
        db.delete_table(u'core_movie')

        # Removing M2M table for field directors on 'Movie'
        db.delete_table(db.shorten_name(u'core_movie_directors'))

        # Deleting model 'CastTranslation'
        db.delete_table(u'core_cast_translation')

        # Deleting model 'Cast'
        db.delete_table(u'core_cast')


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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.movie': {
            'Meta': {'object_name': 'Movie'},
            'actors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'appeared_in_movies'", 'symmetrical': 'False', 'through': "orm['core.Cast']", 'to': "orm['core.Person']"}),
            'directors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'directed_movies'", 'symmetrical': 'False', 'to': "orm['core.Person']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imdb_id': ('django.db.models.fields.CharField', [], {'max_length': '12', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'tmdb_id': ('django.db.models.fields.CharField', [], {'max_length': '12', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'core.movietranslation': {
            'Meta': {'unique_together': "[(u'language_code', u'master')]", 'object_name': 'MovieTranslation', 'db_table': "u'core_movie_translation'"},
            'cover': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'movie'", 'null': 'True', 'to': "orm['core.Image']"}),
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