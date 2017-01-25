from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    if 'is_valid' in request.session:
        request.session.clear()
    return render(request, 'email_app/index.html')

def process(request):
    if request.method == "POST":
        email = request.POST['form_email']
        errors = Email.objects.validate(email)
        if errors:
            messages.error(request, errors)
            return redirect('/')
        success = Email.objects.add_email(email)
        messages.success(request, success)
        request.session['is_valid'] = True
        return redirect('/success')
    return redirect('/')

def success(request):
    emails = Email.objects.all().order_by('-created_at')
    context = {'emails': emails}
    return render(request, 'email_app/success.html', context)

def delete(request, email_id):
    delete = Email.objects.remove(id = email_id)
    messages.success(request, delete)
    return redirect('/success')
