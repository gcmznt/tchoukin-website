# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table('events_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('to_date', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('address_address', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('address_lat', self.gf('django.db.models.fields.FloatField')()),
            ('address_lon', self.gf('django.db.models.fields.FloatField')()),
            ('address_country', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('address_locality', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('address_province', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('address_postal_code', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('address_address_without_number', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('address_address_number', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('confirmation_code', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('insert_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('events', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table('events_event')


    models = {
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'address_address': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'address_address_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address_address_without_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address_country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address_lat': ('django.db.models.fields.FloatField', [], {}),
            'address_locality': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address_lon': ('django.db.models.fields.FloatField', [], {}),
            'address_postal_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address_province': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'confirmation_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'from_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'to_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['events']