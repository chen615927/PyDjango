from django.conf.urls import *

urlpatterns = patterns('dj.views',
    url(r'(?P<year>\d{4})/$', 'home', name='home'),
    url(r'test/', 'testa', name='test'),
)
