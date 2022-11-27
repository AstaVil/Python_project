from django import forms
from  .models import Author, Book, BookReview


class BookUploadForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author','year','desc','pdf', 'cover')

class AuthorUploadForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name','biography','author_photo')

class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ('book','comentReview', 'pdfReview')


