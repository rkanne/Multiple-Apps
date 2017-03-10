from __future__ import unicode_literals
from django.db import models
from ..loginregistration.models import User

class CourseManager(models.Manager):
    def add_user_to_course(self, form_data):
        course = self.get(id=form_data['course'])
        # print course.name
        # print course.id
        user = User.loginMgr.get(id=form_data['user'])
     

class Course(models.Model):
	name = models.CharField(max_length = 255)
	description = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = CourseManager()

