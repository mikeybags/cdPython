from django.shortcuts import render, redirect
from django.contrib import messages
from models import *

# Create your views here.
def index(request):
    courses = Course.objects.filter().order_by('-created_at')
    context = {'courses': courses}
    return render(request, 'course_app/index.html', context)

def add(request):
    if request.method == "POST":
        course = Course(name = request.POST['name'])
        course.save()
        description = Description(course= course, description = request.POST['description'])
        description.save()
    return redirect('/')

def destroy(request, course_id):
    course = Course.objects.get(id=course_id)
    context = {'course': course}
    return render(request, 'course_app/delete.html', context)

def delete(request, course_id):
    if request.method == "POST":
        Course.objects.get(id=course_id).delete()
    return redirect('/')

def comments(request, course_id):
    course_id = Course.objects.get(id = course_id)
    comments = Comment.objects.filter(course_id = course_id)
    context = {'comments': comments,
               'course': course_id}
    return render(request, 'course_app/comments.html', context)

def add_comment(request, course_id):
    if request.method == 'POST':
        comment = Comment(comment = request.POST['comment'], course_id = course_id)
        comment.save()
    return redirect('/courses/'+ str(course_id))
