'''
Created on 16/12/2015

@author: luisza
'''


from django.conf.urls import patterns, url
from crdist.views import  get_distric, get_canton
from django.conf import settings

urlpatterns = patterns('',
                       url('^canton$', get_canton, name="crdist_canton"),
                       url('^district$', get_distric, name="crdist_district"),
                       )

if settings.DEBUG:
    from crdist.tests import view_test_form
    urlpatterns += patterns('', url('^test$', view_test_form),)
