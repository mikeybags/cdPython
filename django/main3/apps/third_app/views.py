from django.shortcuts import render
from models import People


def index(request):

    return render (request, 'third_app/index.html')
