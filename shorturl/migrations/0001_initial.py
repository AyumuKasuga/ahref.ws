# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ShortUrl'
        db.create_table('shorturl_shorturl', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source_url', self.gf('django.db.models.fields.URLField')(max_length=8192)),
            ('short_url', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=0, auto_now_add=True, null=True, blank=True)),
            ('clicks', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, null=True, blank=True)),
        ))
        db.send_create_signal('shorturl', ['ShortUrl'])


    def backwards(self, orm):
        # Deleting model 'ShortUrl'
        db.delete_table('shorturl_shorturl')


    models = {
        'shorturl.shorturl': {
            'Meta': {'object_name': 'ShortUrl'},
            'clicks': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': '0', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_url': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'source_url': ('django.db.models.fields.URLField', [], {'max_length': '8192'})
        }
    }

    complete_apps = ['shorturl']