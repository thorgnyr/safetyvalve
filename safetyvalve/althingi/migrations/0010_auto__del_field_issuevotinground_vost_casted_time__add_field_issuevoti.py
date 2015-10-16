# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'IssueVotingRound.vost_casted_time'
        db.delete_column(u'althingi_issuevotinground', 'vost_casted_time')

        # Adding field 'IssueVotingRound.votes_casted_time'
        db.add_column(u'althingi_issuevotinground', 'votes_casted_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 8, 8, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'IssueVotingRound.vost_casted_time'
        raise RuntimeError("Cannot reverse this migration. 'IssueVotingRound.vost_casted_time' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'IssueVotingRound.vost_casted_time'
        db.add_column(u'althingi_issuevotinground', 'vost_casted_time',
                      self.gf('django.db.models.fields.DateTimeField')(),
                      keep_default=False)

        # Deleting field 'IssueVotingRound.votes_casted_time'
        db.delete_column(u'althingi_issuevotinground', 'votes_casted_time')


    models = {
        u'althingi.document': {
            'Meta': {'object_name': 'Document'},
            'doc_num': ('django.db.models.fields.IntegerField', [], {}),
            'doc_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['althingi.Issue']"}),
            'path_html': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'path_pdf': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'time_published': ('django.db.models.fields.DateTimeField', [], {}),
            'xhtml': ('django.db.models.fields.TextField', [], {})
        },
        u'althingi.issue': {
            'Meta': {'object_name': 'Issue'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'final_vote_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_num': ('django.db.models.fields.IntegerField', [], {}),
            'issue_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['althingi.Session']"})
        },
        u'althingi.issuevotinground': {
            'Meta': {'object_name': 'IssueVotingRound'},
            'final_round': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_parliamentarian_votes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['althingi.Issue']"}),
            'round_details': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'round_number': ('django.db.models.fields.IntegerField', [], {}),
            'round_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'votes_casted_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'althingi.parliamentarian': {
            'Meta': {'object_name': 'Parliamentarian'},
            'constituency': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'constituency_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'most_recent_session_served': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_abbreviation': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5'}),
            'parliamentarian_id': ('django.db.models.fields.IntegerField', [], {}),
            'party': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'seat_number': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'althingi.parliamentarianvote': {
            'Meta': {'object_name': 'ParliamentarianVote'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_voting_round': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['althingi.IssueVotingRound']"}),
            'parliamentarian': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['althingi.Parliamentarian']"}),
            'vote_type': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'althingi.session': {
            'Meta': {'object_name': 'Session'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'session_num': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['althingi']