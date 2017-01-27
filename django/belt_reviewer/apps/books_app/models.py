from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User

class ReviewManager(models.Manager):
    def add_review(self, rating, review, user_id, book):
        errors = []
        if not review:
            errors.append("Review must not be empty.")
        if errors:
            return {'errors': errors}
        user = User.objects.get(id = user_id)
        review = Review.objects.create(rating = rating, review = review, user = user, book = book)
        return {'review': review}

class BookManager(models.Manager):
    def add_book(self, title, author):
        errors = []
        if not title:
            errors.append("Title must not be empty.")
        if not author:
            errors.append("Author must not be empty.")
        if errors:
            return {'errors': errors}
        try:
            book = Book.objects.create(title = title, author = author)
        except IntegrityError:
            errors.append("Book already exists in database. Please go to its page and add a review there.")
            return errors
        return {'book': book}

class Book(models.Model):
    title = models.CharField(max_length = 100, unique = True)
    author = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = BookManager()

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, related_name = "user_reviews")
    book = models.ForeignKey(Book, related_name = "book_reviews")

    objects = ReviewManager()
