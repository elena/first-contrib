# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'KnownFor.project'
        db.alter_column(u'stories_knownfor', 'project', self.gf('django.db.models.fields.CharField')(max_length=256))

        # Changing field 'KnownFor.role'
        db.alter_column(u'stories_knownfor', 'role', self.gf('django.db.models.fields.CharField')(max_length=256))

        # Changing field 'Story.project'
        db.alter_column(u'stories_story', 'project', self.gf('django.db.models.fields.CharField')(max_length=256))

    def backwards(self, orm):

        # Changing field 'KnownFor.project'
        db.alter_column(u'stories_knownfor', 'project', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'KnownFor.role'
        db.alter_column(u'stories_knownfor', 'role', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Story.project'
        db.alter_column(u'stories_story', 'project', self.gf('django.db.models.fields.CharField')(max_length=128))

    models = {
        u'stories.knownfor': {
            'Meta': {'object_name': 'KnownFor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stories.Name']"}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '256'})
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
            'comms': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'blank': 'True'}),
            'comms_other': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'experience': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stories.Name']"}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'project_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'skill_language': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True'}),
            'skill_professional': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True'}),
            'skill_vcs': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True'}),
            'vcs': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'vcs_other': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'year': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['stories']