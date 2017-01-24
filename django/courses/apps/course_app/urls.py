from django.conf.urls import url
from views import index, add, destroy, delete, comments, add_comment

urlpatterns = [
    url(r'^$', index),
    url(r'^add$', add),
    url(r'^courses/destroy/(?P<course_id>\d+)$', destroy),
    url(r'^delete/(?P<course_id>\d+)$', delete),
    url(r'^courses/(?P<course_id>\d+)$', comments),
    url(r'^courses/(?P<course_id>\d+)/comment$', add_comment)
]
