from . import views
from django.urls import path
from jollywood.models import Books

urlpatterns = [
    path('', views.home, name='jollywood-home'),
    path('bookslist/', views.book_list, name='jollywood-bookslist'),
    path('about/', views.about, name='jollywood-about'),
    path('books/<slug>/', views.Books.as_view(extra_context={'title': 'Books'}), name='jollywood-books'),
    path('contact/', views.contact, name='jollywood-contact'),
    path('english/', views.english, name='jollywood-english'),
    path('russian/', views.russian, name='jollywood-russian'),
    path('mathematics/', views.mathematics, name='jollywood-mathematics'),
    path('kids/', views.kids, name='jollywood-kids'),
    path('tests/', views.tests, name='jollywood-tests'),
]
