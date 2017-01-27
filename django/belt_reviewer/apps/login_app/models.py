from __future__ import unicode_literals
from django.db import models
from django.db import IntegrityError
from django.contrib import messages

import bcrypt
import re
# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[A-Za-z\s]+$')

class UserManager(models.Manager):
    def validate(self, name, alias, email, password, confirm_pw):
        errors = []
        if len(name) < 4:
            errors.append("Name must be at least 4 characters.")
        elif not NAME_REGEX.match(name):
            errors.append("Name must contain only letters.")
        if len(alias) > 50:
            errors.append("Alias can be no longer than 50 characters.")
        if not EMAIL_REGEX.match(email):
            errors.append("Please enter a valid e-mail address.")
        if len(password) < 8 or len(password) > 20:
            errors.append("Password must be between 8 and 20 characters")
        if password != confirm_pw:
            errors.append("Passwords do not match. Please re-confirm your password.")
        return errors

    def register(self, name, alias, email, password):
        errors = []
        try:
            hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = User.objects.create(name = name, alias = alias, email = email, pw_hash = hashed)
        except IntegrityError:
            errors.append('E-mail already exists. Please log in or try another e-mail address.')
            return {'errors': errors}
        return {'user': user}

    def authenticate(self, email, password):
        errors = []
        try:
            user = User.objects.get(email = email)
        except:
            errors.append("E-Mail does not exist. Please register!")
            return { 'errors': errors }
        if bcrypt.hashpw(password.encode(), user.pw_hash.encode()) == user.pw_hash:
            return { 'user': user }
        errors.append("Password is incorrect. Please re-enter your password.")
        return { 'errors': errors }

class User(models.Model):
    name = models.CharField(max_length = 75)
    alias = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50, unique = True)
    pw_hash = models.CharField(max_length = 256)

    objects = UserManager()
