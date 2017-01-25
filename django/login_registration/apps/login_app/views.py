from django.shortcuts import render, redirect
from models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login_app/index.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_pw = request.POST['confirm_pw']
        user = User.objects.authenticate(first_name, last_name, email, password, confirm_pw)
        if not user:
            user = User.objects.register(first_name, last_name, email, password)
            if 'errors' in user:
                for error in user['errors']:
                    messages.error(request, error)
                return redirect('/')
            request.session['first_name'] = first_name
            return redirect('/success')
        for error in user['errors']:
            messages.error(request, error)
        return redirect('/')
    return redirect('/')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        login = User.objects.login(email, password)
        if 'errors' in login:
            for error in login['errors']:
                messages.error(request, error)
                return redirect('/')
        request.session['first_name'] = login['user'].first_name
    return redirect('/success')

def logout(request):
    request.session.clear()
    return redirect('/')

def success(request):
    return render(request, 'login_app/success.html')
