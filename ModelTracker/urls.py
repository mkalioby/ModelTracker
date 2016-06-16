from django.conf.urls import patterns, include, url
import ModelTracker
import debug_toolbar

urlpatterns = patterns('',
   url(r'^__debug__/', include(debug_toolbar.urls)),
    url('^$','ModelTracker.views.main',name="main"),
                       )
