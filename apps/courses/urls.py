from django.conf.urls import url
from . import views

app_name = 'course'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^courses/destroy/(?P<id>\d+)$', views.course, name='course'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^logout$', views.logout, name='logout'),
]