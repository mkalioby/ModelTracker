try:
    from django.conf.urls import url
except:
    from django.urls import path as url
from . import views

urlpatterns = [
    url('^$',views.main,name="main"),
                       ]
