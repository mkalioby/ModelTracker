from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.main,name="main"),
    url('show/',views.showChanges,name="showModelChanges"),
    url('get/',views.getChanges,name="getModelChanges"),
                       ]
