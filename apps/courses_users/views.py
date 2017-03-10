from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Count
from .models import Course
from ..loginregistration.models import User
from ..courses_users.models import User_Course

# Create your views here.
def index(request):
	
    context = {
    	'users' : User.objects.all(),
        'courses' : Course.objects.all().annotate(usercount=Count('usercourse')),
    }
    return render(request, 'courses_users/index.html', context)

def add_user_to_course(request):
    # print " inside add_user_to_course"
    add_user_to_course = User_Course.objects.create(user_id=request.POST['user'], course_id = request.POST['course'])
    # print "Course Value ==" , request.POST['course']
    return redirect(reverse('course_user:index'))