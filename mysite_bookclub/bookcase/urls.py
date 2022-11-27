from django.urls import path
from . import views


urlpatterns = [
    path('', views.homeScreenView, name="home"),

    path('authors/', views.authors_list, name='authors_list'),
    path('authors/upload', views.upload_author, name='upload_author'),
    path('author/<int:id>', views.get_author, name= "author"),

    path('books/', views.books_list, name='books_list'),
    path('books/upload', views.upload_book, name='upload_book'),
    path('allbooks/<int:id>/', views.delete_book, name='delete_book'),
    path('book/<int:id>', views.get_book, name="bookdetail"),
    path('bsearch/', views.search_book, name='search_book'),


    path('reviews/', views.reviews_list, name='reviews_list'),
    path('book/send_review', views.send_review, name='send_review'),

    path('renewal/', views.message_renewal, name="message_renewal"),

]
