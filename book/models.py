from django.contrib.auth.models import User
from django.db import models
from isbn_field import ISBNField

from shelf.models import Shelf
import datetime
import uuid

# Create your models here.


class Book(models.Model):
    isbn = ISBNField()
    title = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    category = models.CharField(max_length=50)
    author = models.CharField(max_length=80)
    publisher = models.CharField(max_length=80)
    publications_date = models.DateField(default=datetime.date.today, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"Author: {self.author} | Title: {self.title} | Category: {self.category}"
        )


class BookItem(models.Model):
    shelf = models.ManyToManyField(Shelf, blank=True)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4(), editable=False)
    reserve = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
        related_name="reserve",
    )
    is_reserve = models.BooleanField(default=False)
    rent = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
        related_name="rent",
    )
    is_rent = models.BooleanField(default=False)

    def __str__(self):
        return f"Book: {self.Book} | Rent: {self.is_rent} | Reserved: {self.is_reserve}"
