from django.conf.urls import url

from views import index, randomize

urlpatterns = [
    url(r'^$', index),
    url(r'^randomize$', randomize),
]
