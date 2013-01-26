# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Link'
        db.create_table('url_shortener_link', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clicks', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
        ))
        db.send_create_signal('url_shortener', ['Link'])


    def backwards(self, orm):
        # Deleting model 'Link'
        db.delete_table('url_shortener_link')


    models = {
        'url_shortener.link': {
            'Meta': {'object_name': 'Link'},
            'clicks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['url_shortener']