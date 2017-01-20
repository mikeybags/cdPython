from django.conf.urls import url
from views import index, process_money

urlpatterns = [
    url(r'^$', index),
    url(r'^process_money/(?P<choice>\w+)$', process_money),
    ]
