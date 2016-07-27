from django.conf.urls import url
from . import views

app_name = 'ticker'

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^event/add/$', views.EventAdd.as_view(), name="event-add"),
    url(r'^event/edit/(?P<pk>\d+)/$', views.EventEdit.as_view(), name="event-edit"),
    url(r'^event/delete/(?P<pk>\d+)/$', views.EventDelete.as_view(), name="event-delete"),
]
