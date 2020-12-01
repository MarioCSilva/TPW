from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from app.forms import BookQueryForm, AuthorQueryForm, AutPubQueryForm
from app.models import Book
from app.models import Author
from app.models import Publisher


def load_books(request):
    data = {
        'data': Book.objects.all()
    }
    return render(request, 'books.html', data)


def load_book_details(request, num):
    data = {
        'data': Book.objects.get(id=num)
    }
    return render(request, 'book_details.html', data)


def load_authors(request):
    data = {
        'data': Author.objects.all()
    }
    return render(request, 'authors.html', data)


def load_author_details(request, num):
    data = {
        'data': Author.objects.get(id=num)
    }
    return render(request, 'author_details.html', data)


def load_author_books(request, num):
    name = Author.objects.get(id=num)
    data = {
        'data': Book.objects.filter(authors=name)
    }
    return render(request, 'author_books.html', data)


def load_publishers(request):
    data = {
        'data': Publisher.objects.all()
    }
    return render(request, 'publishers.html', data)


def load_publisher_details(request, num):
    data = {
        'data': Publisher.objects.get(id=num)
    }
    return render(request, 'publisher_details.html', data)


def bookquery(request):
    if request.method == 'POST':
        form = BookQueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            books = Book.objects.filter(title__contains=query)
            return render(request, 'booklist.html', {'boks': books, 'query': query})
    else:
        form = BookQueryForm()
    return render(request, 'bookquery.html', {'form': form})


def authorquery(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.info(request, 'Your must be logged in!')
            return redirect('/login')
        form = AuthorQueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            authors = Author.objects.filter(name__contains=query)
            return render(request, 'authorlist.html', {'auths': authors, 'query': query})
    else:
        form = AuthorQueryForm()
    return render(request, 'authorquery.html', {'form': form})


def autpubquery(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('/login')
        form = AutPubQueryForm(request.POST)
        if form.is_valid():
            aut = form.cleaned_data['aut']
            pub = form.cleaned_data['pub']
            query=""
            if aut != "":
                query += " author "+aut
            if pub != "":
                query += " publisher "+pub
            books = Book.objects.filter(authors__name__contains=aut, publisher__name__contains=pub)
            return render(request, 'booklist.html', {'boks': books, 'query': query})
    else:
        form = AutPubQueryForm()
    return render(request, 'autpubquery.html', {'form': form})


def load_publisher_authors(request, num):
    return render(request, 'author_books.html', {'data': Author.objects.filter(id__in=Book.objects.filter(publisher=Publisher.objects.get(id=num)).values_list('authors').distinct())})
