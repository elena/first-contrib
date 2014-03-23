# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Name'
        db.create_table(u'stories_name', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('preferred_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('github', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('other', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'stories', ['Name'])

        # Adding model 'KnownFor'
        db.create_table(u'stories_knownfor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stories.Name'])),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('project', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'stories', ['KnownFor'])

        # Adding model 'Story'
        db.create_table(u'stories_story', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stories.Name'])),
            ('project', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('project_description', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('vcs', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('vcs_other', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('month', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True)),
            ('year', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('experience', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('skill_professional', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('skill_language', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('skill_vcs', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('added_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'stories', ['Story'])


    def backwards(self, orm):
        # Deleting model 'Name'
        db.delete_table(u'stories_name')

        # Deleting model 'KnownFor'
        db.delete_table(u'stories_knownfor')

        # Deleting model 'Story'
        db.delete_table(u'stories_story')


    models = {
        u'stories.knownfor': {
            'Meta': {'object_name': 'KnownFor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stories.Name']"}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'stories.name': {
            'Meta': {'object_name': 'Name'},
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'github': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'other': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'preferred_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'stories.story': {
            'Meta': {'object_name': 'Story'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'experience': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stories.Name']"}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'project_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'skill_language': ('django.db.models.fields.SmallIntegerField', [], {}),
            'skill_professional': ('django.db.models.fields.SmallIntegerField', [], {}),
            'skill_vcs': ('django.db.models.fields.SmallIntegerField', [], {}),
            'vcs': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'vcs_other': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'year': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['stories']