from django.conf.urls import url
from django.contrib import admin

from views import *

urlpatterns = [
    url(r'^$', index, name="home"),
    url(r'^add$', add, name="add"),
    url(r'^add_book$', add_book, name="add_book"),
    url(r'^books/(?P<id>\d+)$', book, name="book"),
    url(r'^books/(?P<id>\d+)/add_review/$', add_review, name="add_review"),
    url(r'^users/(?P<id>\d+)$', user_profile, name="user_profile"),
    url(r'^reviews/delete/(?P<id>\d+)$', delete_review, name="delete_review"),    
]
