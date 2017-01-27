from django.shortcuts import render, redirect
from models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login_app/index.html')

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        alias = request.POST['alias']
        email = request.POST['email']
        password = request.POST['password']
        confirm_pw = request.POST['confirm_pw']
        request.session['name'] = name
        request.session['alias'] = alias
        request.session['email'] = email
        errors = []
        errors += User.objects.validate(name, alias, email, password, confirm_pw)
        if errors:
            for error in errors:
                messages.error(request, error)
        else:
            registration = User.objects.register(name, alias, email, password)
            if 'errors' in registration:
                for error in registration['errors']:
                    messages.error(request, error)
            if 'user' in registration:
                request.session['id'] = registration['user'].id
                return redirect('books:home')
    return redirect('login:index')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        request.session['login_email'] = email
        login = User.objects.authenticate(email, password)
        if 'errors' in login:
            for error in login['errors']:
                messages.error(request, error)
        else:
            request.session['alias'] = login['user'].alias
            request.session['id'] = login['user'].id
            return redirect('books:home')
    return redirect('login:index')

def logout(request):
    request.session.clear()
    return redirect('login:index')

def success(request):
    return render(request, 'login_app/success.html')
