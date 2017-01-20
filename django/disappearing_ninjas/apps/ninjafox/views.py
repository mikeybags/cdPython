from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'ninjafox/index.html')

def ninja(request, color):
    ninja = {'color': color}
    return render(request, 'ninjafox/ninjafox.html', ninja)

def ninjas(request):
    return render(request, 'ninjafox/ninjas.html')
