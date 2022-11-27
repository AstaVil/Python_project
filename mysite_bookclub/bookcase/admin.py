from django.contrib import admin
from . models import Book, Author, BookReview

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('id', 'book__title', 'book__author')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'display_books')
    search_fields = ('id', 'author__last_name')

class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'review_date', 'comentReview', 'pdfReview')
    search_fields = ('user__username', 'book__title')


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookReview, BookReviewAdmin)


