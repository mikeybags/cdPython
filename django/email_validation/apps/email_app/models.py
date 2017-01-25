from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import re

# Create your models here.
class EmailManager(models.Manager):
    def validate(self, email):
        errors = ''
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(email):
            errors = "Please enter a valid e-mail address!"
        try:
            Email.objects.get(email=email)
            errors = 'E-mail has already been entered. Only unique e-mails are allowed.'
        except:
            return errors
        return errors

    def add_email(self, email):
        Email.objects.create(email = email)
        success = "The email address you entered " + email + " is a VALID email address. Thank you!"
        return success

    def remove(self, id):
        email = Email.objects.get(id = id)
        success = email.email + " has been removed from the list!"
        email.delete()
        return success

class Email(models.Model):
    email = models.EmailField(max_length = 100, unique = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = EmailManager()
