from django.conf.urls import *

urlpatterns = patterns('news.views',
    url(r'^$', 'index', name='index'),
)
