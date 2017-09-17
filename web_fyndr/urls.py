from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^map/$', views.map, name='map'),
        url(r'^get_rooms/$', views.find_rooms, name='map'),

        ]
