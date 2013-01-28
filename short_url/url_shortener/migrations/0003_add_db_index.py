# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Link', fields ['code']
        db.create_index('url_shortener_link', ['code'])


    def backwards(self, orm):
        # Removing index on 'Link', fields ['code']
        db.delete_index('url_shortener_link', ['code'])


    models = {
        'url_shortener.link': {
            'Meta': {'object_name': 'Link'},
            'clicks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '512', 'blank': 'True'})
        }
    }

    complete_apps = ['url_shortener']