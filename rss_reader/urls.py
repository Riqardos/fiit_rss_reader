from django.conf.urls import url
from django.urls import path

from rss_reader.views import view_rss

urlpatterns = [
    path('', view_rss, name='home'),
]
