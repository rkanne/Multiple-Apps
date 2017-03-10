from django.conf.urls import url
from . import views

app_name = 'course_user'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_user_to_course$', views.add_user_to_course, name='add_user_to_course'),
]