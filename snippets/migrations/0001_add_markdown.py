
from south.db import db
from django.db import models
from snippets.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Snippet.markdown'
        db.add_column('snippets_snippet', 'markdown', models.BooleanField(default=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Snippet.markdown'
        db.delete_column('snippets_snippet', 'markdown')
        
    
    
    models = {
        'snippets.snippet': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'markdown': ('models.BooleanField', [], {'default': 'True'}),
            'name': ('models.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'value': ('models.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['snippets']
