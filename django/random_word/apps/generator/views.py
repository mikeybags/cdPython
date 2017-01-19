from django.shortcuts import render, redirect
import string
import random

def randomizer(size=14, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    return render(request, 'generator/index.html')

def randomize(request):
    if request.method == "POST":
        random_word = randomizer()
        request.session['random_word'] = random_word
        request.session['counter'] += 1
        return redirect('/')
