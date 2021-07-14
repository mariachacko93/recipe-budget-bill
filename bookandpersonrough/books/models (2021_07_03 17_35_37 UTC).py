from django.db import models

class Book(models.Model):
    bookname=models.CharField(max_length=120)
    price=models.IntegerField()
    pages=models.IntegerField()
    author=models.CharField(max_length=120)

    def __str__(self):
        return self.bookname


