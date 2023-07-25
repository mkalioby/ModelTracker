try:
    from django.urls import re_path
except ModuleNotFoundError:
    from django.conf.urls import re_path
from . import views

urlpatterns = [
    re_path('^$',views.test,name="test"),
]