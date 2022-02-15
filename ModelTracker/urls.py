from django.conf.urls import url,re_path
from . import views

urlpatterns = [
    url('^$',views.main,name="main"),
    url('show/',views.showChanges,name="showModelChanges"),
    re_path(r'revert/(\d+)',views.revert,name="revert"),
    url('get/',views.getChanges,name="getModelChanges"),
                       ]
