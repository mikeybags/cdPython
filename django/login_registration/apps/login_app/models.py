from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

import bcrypt
import re
# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[A-Za-z]+$')

class UserManager(models.Manager):
    def authenticate(self, first, last, email, password, confirm_pw):
        errors = []
        if len(first) < 2:
            errors.append("First name must be at least 2 characters.")
        elif not NAME_REGEX.match(first):
            errors.append("First name must contain only letters.")
        if len(last) < 2:
            errors.append("Last name must be at least 2 characters.")
        elif not NAME_REGEX.match(last):
            errors.append("Last name must contain only letters.")
        if not EMAIL_REGEX.match(email):
            errors.append("Please enter a valid e-mail address.")
        if len(password) < 8:
            errors.append("Password must be between 8 and 20 characters")
        if password != confirm_pw:
            errors.append("Passwords do not match. Please re-confirm your password.")
        if errors:
            return { 'errors': errors }
        else:
            return errors

    def register(self, first, last, email, password):
        errors = []
        try:
            user = User.objects.get(email = email)
            errors.append("E-mail already exists. Please log in or try another e-mail address.")
            return { 'errors': errors }
        except ObjectDoesNotExist:
            user = 0
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user = User.objects.create(first_name = first, last_name = last, email = email, pw_hash = pw_hash)
        return {'user': user}

    def login(self, email, password):
        errors = []
        try:
            user = User.objects.get(email = email)
        except:
            errors.append("E-Mail does not exist. Please register!")
            return { 'errors': errors }
        if user:
            if bcrypt.hashpw(password.encode(), user.pw_hash.encode()) == user.pw_hash:
                return {'user': user}
            errors.append("Password is incorrect. Please re-enter your password.")
            return {'errors': errors}

class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50, unique = True)
    pw_hash = models.CharField(max_length = 20)

    objects = UserManager()
