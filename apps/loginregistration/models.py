from __future__ import unicode_literals
from django.db import models

import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$') 
PASSWORD_REGEX = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{8,}$')
TEXTBOX_REGEX = re.compile(r'^[a-zA-Z]+$')  

# Create your models here.
class UserManager(models.Manager):
    def register(self, first_name, last_name, email, password, confirm_password):
        message = []
        if len(first_name) <2 and len(last_name) <2:
        	message.append("Your first name and last name should not contain fewer than 2 characters!!")
        elif not TEXTBOX_REGEX.match(first_name) and TEXTBOX_REGEX.match(last_name):
        	message.append("First Name contains letters only!!")
        if len(email) == 0:
            message.append("Email is required")
        elif not EMAIL_REGEX.match(email):
        	message.append("Email is not VALID!!")
        	if len(password) == 0:
        		message.append("Password is required")
        elif not PASSWORD_REGEX.match(password):
            message.append("Password is not VALID!!")
        if len(password) < 1:
        	message.append("Password cannot be blank!")
        if len(confirm_password) < 1:
        	message.append("Confirm Password cannot be blank!")
        if password != confirm_password:
        	message.append("Passwords do not match.")
        if len(message) != 0:
            return (False, message)
        else:
        	pw_hash = bcrypt.hashpw(str(password), bcrypt.gensalt())
        	registration = User.objects.create(first_name=first_name,last_name=last_name, email=email, password=pw_hash)
        	registration.save()
        return (True, registration)

    def login(self, email, password):
        login_message = []
        if len(email) == 0:
            login_message.append("Email cannot be blank!")
        elif len(email) > 1:
            if not EMAIL_REGEX.match(email):
                login_message.append("Email is not VALID!!")
            login = User.objects.filter(email=email)
            if len(login) < 1:
                login_message.append("Email does not exist in database")
        if len(password) == 0:
                login_message.append("Password cannot be blank!")
        elif not PASSWORD_REGEX.match(password):
            login_message.append("Password is not VALID!!")
        if len(login_message) != 0:
            return (False, login_message)
        else:
            # print "False======"
            login = User.objects.filter(email=email)
            if len(login) < 1:
                login_message.append("User does not exist in database")
            elif (bcrypt.checkpw(str(password),str(login[0].password))):
                return(True, login[0])
            else:
                login_message.append("Password is incorrect please try again")
                return (False, login_message)
                
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()



