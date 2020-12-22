"""aula3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_page'),
    path('books/', views.load_books, name='books_page'),
    path('book_details/<int:num>', views.load_book_details, name='book_details_page'),
    path('authors/', views.load_authors, name='authors_page'),
    path('author_details/<int:num>', views.load_author_details, name='author_details_page'),
    path('author_books/<int:num>', views.load_author_books, name='author_books_details_page'),
    path('publishers/', views.load_publishers, name='publishers_page'),
    path('publisher_details/<int:num>', views.load_publisher_details, name='publisher_details_page'),
    path('publisher_authors/<int:num>', views.load_publisher_authors, name='publisher_authors_details_page'),
    path('bookquery/', views.bookquery, name='bookquery'),
    path('authorquery/', views.authorquery, name='authorquery'),
    path('autpubquery/', views.autpubquery, name='autpubquery'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='login/'), name='logout'),
    path('ws/author', views.get_author),
]
