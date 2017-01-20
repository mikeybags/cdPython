from django.conf.urls import url
from views import index, ninja, ninjas

urlpatterns = [
    url(r'^$', index),
    url(r'^ninjas/(?P<color>\w+)$', ninja),
    url(r'^ninjas$', ninjas),
]
