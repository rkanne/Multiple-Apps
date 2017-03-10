from __future__ import unicode_literals

from django.db import models
from ..loginregistration.models import User
from ..courses.models import Course

# Create your models here.
class User_Course(models.Model):
	user = models.ForeignKey(User, related_name="courseuser")
	course = models.ForeignKey(Course, related_name="usercourse")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
