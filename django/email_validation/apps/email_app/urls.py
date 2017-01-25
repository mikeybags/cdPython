from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^$', index ),
    url(r'^process$', process),
    url(r'^success$', success),
    url(r'^delete/(?P<email_id>\d+)$', delete)
]
