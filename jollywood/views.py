from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Books


def home(request):
	context = {
		'posts': Post.objects.all()[::-1],
		'title': 'Main Page',
		'Beginner': 'Beginner',
		'Elementary': 'Elementary',
		'Pre': 'Pre',
		'Intermediate': 'Intermediate',
		'Upper': 'Upper',
		'Advanced': 'Advanced',
	}
	return render(request, 'index.html', context)


def about(request):
	return render(request, 'about.html', {'title': 'About Page'})


def contact(request):
	return render(request, 'contact.html', {'title': 'Contact Page'})


def english(request):
	return render(request, 'english.html', {'title': 'English'})


def russian(request):
	return render(request, 'russian.html', {'title': 'Russian'})


def mathematics(request):
	return render(request, 'mathematics.html', {'title': 'Mathematics'})


def kids(request):
	return render(request, 'kids.html', {'title': 'Kids'})


def book_list(request):
	context = {
		'title': 'Books List',
		'Beginner': 'Beginner',
		'Elementary': 'Elementary',
		'Pre': 'Pre',
		'Intermediate': 'Intermediate',
		'Upper': 'Upper',
		'Advanced': 'Advanced',
	}
	return render(request, 'all_books.html', context)


def tests(request):
	return render(request, 'tests.html', {'title': 'Tests'})


class Books(ListView):
	model = Books
	slug_field = 'level'
	template_name = 'books.html'
	context_object_name = 'books'