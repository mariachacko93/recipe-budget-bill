from django.shortcuts import render
from books.forms import BookCreateForm
from django.http import HttpResponse
from books.models import Book
# Create your views here.

def createBook(request):
    form=BookCreateForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BookCreateForm(request.POST)
        if form.is_valid():
            bookname = form.cleaned_data.get("bookname")
            price = form.cleaned_data.get("price")
            pages = form.cleaned_data.get("pages")
            author = form.cleaned_data.get("author")
            print(bookname, ",", price, ",", pages, ",", author)
            book = Book(bookname=bookname, price=price, pages=pages, author=author)
            book.save()
            return render(request,"books/booklist.html",context)
    return render(request, "books/createbook.html", context)

def booklist(request):
    books=Book.objects.all()
    context={}
    context["books"]=books
    return render(request,"books/booklist.html",context)