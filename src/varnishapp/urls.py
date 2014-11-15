# this does not work in Django 1.6
#from django.conf.urls.defaults import *
from django.conf.urls import patterns, url, include
from django.conf import settings
from manager import VarnishManager


urlpatterns = patterns('varnishapp.views',
    (r'', 'management'),
)
