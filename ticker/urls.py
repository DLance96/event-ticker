from django.conf.urls import url
from . import views

app_name = 'ticker'

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^event/add/$', views.EventAdd.as_view(), name="event-add"),
]
