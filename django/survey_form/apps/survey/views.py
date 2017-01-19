from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def index(request):
    form_choices = { 'location': ['Chicago', 'Dallas', 'San Francisco', 'Seattle'],
                     'language': ['JavaScript', 'Python', 'Ruby'] }
    return render(request, 'survey/index.html' , form_choices)

def process(request):
    if request.method == "POST":
        is_valid = True
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comments'] = request.POST['comments']
        if len(request.session['name']) < 2:
            is_valid = False
            messages.warning(request, 'Name must be at least 2 characters.')

        if len(request.session['comments']) >140 :
            is_valid = False
            messages.warning(request, 'Comments must be 140 characters or less.')

        if is_valid:
            if 'counter' not in request.session:
                request.session['counter'] = 1
            else:
                request.session['counter'] += 1

            return redirect('/results')
        return redirect('/')

def results(request):
    return render(request, 'survey/results.html')
