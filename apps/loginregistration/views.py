from django.shortcuts import render, redirect , HttpResponse
from django.urls import reverse
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'loginregistration/index.html')

def register(request):
	if request.method == "POST":
		result = User.objects.register(request.POST['first_name'],request.POST['last_name'],request.POST['email'],request.POST['password'],request.POST['confirm_password'])
		# print "result===",result
	 	if result[0]:
	 		# print result[0], "="*20,result[1].name
	 		request.session['name'] = result[1].first_name
	 		request.session['user_id'] = result[1].id
	 		return redirect('/courses')
	 	else:
	 		# print result[0], "="*20
	 		for x in xrange(len(result[1])):
	 			print x
	 			messages.error(request, result[1][x])

	 		return redirect(reverse('index'))

def login(request):
	if request.method == "GET":
		return redirect(reverse('index'))
	if request.method == "POST":
		# print request.POST['email_login'],request.POST['password_login']
		result = User.objects.login(request.POST['email_login'],request.POST['password_login'])
		login = User.objects.filter(email=request.POST['email_login'])
		if result == None:
			messages.error(request, "Your account is invalid")
			return redirect(reverse('index'))
		else:
			users = User.objects.all()
			if len(login)> 0:
				login = login[0].id, login[0].first_name
				request.session['user_id'] = login
				print result[1]
			if result[0]:
		 		request.session['name'] = result[1].first_name
		 		request.session['user_id'] = result[1].id
		 		return redirect('/courses')
		 	else:
		 		for x in xrange(len(result[1])):
		 			messages.error(request, result[1][x])
		 		return redirect(reverse('index'))

def success(request):
	result = User.objects.all()
	context = {
			'result': result,
			'first_name' : request.session.get('first_name')
			}
	return render(request, 'loginregistration/success.html',context)


