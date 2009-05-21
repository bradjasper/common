"""
    Category URLS
"""

from django.conf.urls.defaults import patterns
from views import category

urlpatterns = patterns('categories.views',
    (r'^/(?P<slug>.*).html', 'category'),
    (r'^.html', 'category', {'slug': None}),
)

