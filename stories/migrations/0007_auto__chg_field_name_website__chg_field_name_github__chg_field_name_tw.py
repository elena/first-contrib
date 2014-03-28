# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Name.website'
        db.alter_column(u'stories_name', 'website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Name.github'
        db.alter_column(u'stories_name', 'github', self.gf('django.db.models.fields.CharField')(max_length=128, null=True))

        # Changing field 'Name.twitter'
        db.alter_column(u'stories_name', 'twitter', self.gf('django.db.models.fields.CharField')(max_length=128, null=True))

        # Changing field 'Name.preferred_name'
        db.alter_column(u'stories_name', 'preferred_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True))

        # Changing field 'Name.other'
        db.alter_column(u'stories_name', 'other', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Name.full_name'
        db.alter_column(u'stories_name', 'full_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True))

    def backwards(self, orm):

        # Changing field 'Name.website'
        db.alter_column(u'stories_name', 'website', self.gf('django.db.models.fields.URLField')(default='', max_length=200))

        # Changing field 'Name.github'
        db.alter_column(u'stories_name', 'github', self.gf('django.db.models.fields.CharField')(default='', max_length=128))

        # Changing field 'Name.twitter'
        db.alter_column(u'stories_name', 'twitter', self.gf('django.db.models.fields.CharField')(default='', max_length=128))

        # User chose to not deal with backwards NULL issues for 'Name.preferred_name'
        raise RuntimeError("Cannot reverse this migration. 'Name.preferred_name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Name.preferred_name'
        db.alter_column(u'stories_name', 'preferred_name', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'Name.other'
        db.alter_column(u'stories_name', 'other', self.gf('django.db.models.fields.URLField')(default='', max_length=200))

        # Changing field 'Name.full_name'
        db.alter_column(u'stories_name', 'full_name', self.gf('django.db.models.fields.CharField')(default='', max_length=128))

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
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'github': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'other': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'preferred_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'stories.story': {
            'Meta': {'object_name': 'Story'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'comms': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'comms_other': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'experience': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stories.Name']", 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'project_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'skill_language': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'skill_professional': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'skill_vcs': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vcs': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'vcs_other': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['stories']