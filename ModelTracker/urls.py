from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url('^$','ModelTracker.views.main',name="main"),
                       )
