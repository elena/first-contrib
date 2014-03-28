# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Story.project_description'
        db.alter_column(u'stories_story', 'project_description', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'Story.comms'
        db.alter_column(u'stories_story', 'comms', self.gf('django.db.models.fields.CharField')(max_length=2048, null=True))

        # Changing field 'Story.vcs_other'
        db.alter_column(u'stories_story', 'vcs_other', self.gf('django.db.models.fields.CharField')(max_length=512, null=True))

        # Changing field 'Story.experience'
        db.alter_column(u'stories_story', 'experience', self.gf('ckeditor.fields.RichTextField')(null=True))

        # Changing field 'Story.project'
        db.alter_column(u'stories_story', 'project', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'Story.vcs'
        db.alter_column(u'stories_story', 'vcs', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True))

        # Changing field 'Story.comms_other'
        db.alter_column(u'stories_story', 'comms_other', self.gf('django.db.models.fields.CharField')(max_length=512, null=True))

    def backwards(self, orm):

        # Changing field 'Story.project_description'
        db.alter_column(u'stories_story', 'project_description', self.gf('django.db.models.fields.CharField')(default='', max_length=256))

        # Changing field 'Story.comms'
        db.alter_column(u'stories_story', 'comms', self.gf('django.db.models.fields.CharField')(default='', max_length=2048))

        # Changing field 'Story.vcs_other'
        db.alter_column(u'stories_story', 'vcs_other', self.gf('django.db.models.fields.CharField')(default='', max_length=512))

        # Changing field 'Story.experience'
        db.alter_column(u'stories_story', 'experience', self.gf('ckeditor.fields.RichTextField')(default=''))

        # Changing field 'Story.project'
        db.alter_column(u'stories_story', 'project', self.gf('django.db.models.fields.CharField')(default='', max_length=256))

        # Changing field 'Story.vcs'
        db.alter_column(u'stories_story', 'vcs', self.gf('django.db.models.fields.CharField')(default='', max_length=1024))

        # Changing field 'Story.comms_other'
        db.alter_column(u'stories_story', 'comms_other', self.gf('django.db.models.fields.CharField')(default='', max_length=512))

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