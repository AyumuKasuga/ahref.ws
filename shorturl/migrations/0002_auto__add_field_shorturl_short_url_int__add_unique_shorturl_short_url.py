# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ShortUrl.short_url_int'
        db.add_column('shorturl_shorturl', 'short_url_int',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding unique constraint on 'ShortUrl', fields ['short_url']
        db.create_unique('shorturl_shorturl', ['short_url'])


    def backwards(self, orm):
        # Removing unique constraint on 'ShortUrl', fields ['short_url']
        db.delete_unique('shorturl_shorturl', ['short_url'])

        # Deleting field 'ShortUrl.short_url_int'
        db.delete_column('shorturl_shorturl', 'short_url_int')


    models = {
        'shorturl.shorturl': {
            'Meta': {'object_name': 'ShortUrl'},
            'clicks': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': '0', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_url': ('django.db.models.fields.CharField', [], {'max_length': '128', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'short_url_int': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'source_url': ('django.db.models.fields.URLField', [], {'max_length': '8192'})
        }
    }

    complete_apps = ['shorturl']