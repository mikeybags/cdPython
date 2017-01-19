from django.shortcuts import render, HttpResponse
from datetime import datetime


def index(request):
    time = datetime.now()
    current_time = {'time': time}
    return render(request, 'timedisplay/index.html', current_time)
