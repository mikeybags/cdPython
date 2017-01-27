from django.shortcuts import render, redirect
from models import *
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    if 'id' not in request.session:
        redirect('login:index')
    reviews = Review.objects.filter().order_by('-created_at')[:3]
    books = Book.objects.filter().filter(book_reviews__gt=0).distinct()
    context = {'reviews': reviews,
               'books': books}
    return render(request, 'books_app/home.html', context)

def add(request):
    authors = Book.objects.all().order_by('author').distinct()
    context = {'authors': authors}
    return render(request, 'books_app/add.html', context)

def add_book(request):
    if request.method == "POST":
        title = request.POST['title']
        if request.POST['new_author']:
            author = request.POST['new_author']
        else:
            author = request.POST['author']
        review = request.POST['review']
        rating = request.POST['rating']
        user_id = request.session['id']
        book = Book.objects.add_book(title, author)
        if 'errors' in book:
            for error in book['errors']:
                message.error(request, error)
                return redirect('books:add')
        review = Review.objects.add_review(rating, review, user_id, book['book'])
        return redirect(reverse('books:book', kwargs={'id':book['book'].id}))
    return redirect('books:home')

def book(request, id):
    book = Book.objects.get(id = id)
    reviews = Review.objects.filter(book = book).order_by('-created_at')
    books = Book.objects.all()
    context = {'book': book,
               'reviews': reviews}
    return render(request, 'books_app/book.html', context)

def add_review(request, id):
    if request.method == "POST":
        book = Book.objects.get(id = id)
        review = request.POST['review']
        rating = request.POST['rating']
        user_id = request.session['id']
        review = Review.objects.add_review(rating, review, user_id, book)
        if 'errors' in review:
            for error in review['errors']:
                message.error(request.error)
                return redirect('books:book', id=book.id)
    return redirect('books:book', id=book.id)

def user_profile(request, id):
    user = User.objects.get(id = id)
    books = Book.objects.filter(book_reviews__user = user)
    context = {'user': user,
               'books': books}
    return render(request, 'books_app/profile.html', context)

def delete_review(request, id):
    Review.objects.get(id = id).delete()
    return redirect('books:home')
