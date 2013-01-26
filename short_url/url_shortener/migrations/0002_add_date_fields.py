# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Link.created'
        db.add_column('url_shortener_link', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 1, 26, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Link.updated'
        db.add_column('url_shortener_link', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 1, 26, 0, 0), blank=True),
                      keep_default=False)


        # Changing field 'Link.url'
        db.alter_column('url_shortener_link', 'url', self.gf('django.db.models.fields.URLField')(max_length=512))

    def backwards(self, orm):
        # Deleting field 'Link.created'
        db.delete_column('url_shortener_link', 'created')

        # Deleting field 'Link.updated'
        db.delete_column('url_shortener_link', 'updated')


        # Changing field 'Link.url'
        db.alter_column('url_shortener_link', 'url', self.gf('django.db.models.fields.URLField')(max_length=200))

    models = {
        'url_shortener.link': {
            'Meta': {'object_name': 'Link'},
            'clicks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '512', 'blank': 'True'})
        }
    }

    complete_apps = ['url_shortener']