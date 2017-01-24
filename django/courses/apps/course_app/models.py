from __future__ import unicode_literals
from django.db import models

import datetime
from django.utils import timezone

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Description(models.Model):
    description = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    course = models.OneToOneField(Course, primary_key=True, on_delete = models.CASCADE)

class Comment(models.Model):
    comment = models.TextField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    course = models.ForeignKey(Course)
