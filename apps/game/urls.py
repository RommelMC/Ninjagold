from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^process_money/(?P<place>[a-z]+)$', views.money),
    url(r'^restart$', views.clear),
    url(r'^token$', views.token),
]

