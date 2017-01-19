from django.conf.urls import url

from views import index, process, results

urlpatterns = [
    url(r'^$', index),
    url(r'^surveys/process$', process),
    url(r'^results$', results)
]
