from django.db import models

from django.conf import settings
from django.urls import reverse



class Book(models.Model):
    title = models.CharField('Knygos pavadinimas', max_length=200)
    author = models.ForeignKey('Author', null=True, on_delete=models.SET_NULL, related_name='books')
    year = models.CharField('Metai', max_length=4, null=True, blank=True)
    desc = models.TextField('Aprašymas', max_length=2000, null=True, blank=True)
    pdf = models.FileField('Knygos pdf', upload_to='books/pdfs/', null=True, blank=True)
    cover = models.ImageField('Viršelis', max_length=50, upload_to='books/covers/', null=True, blank=True)

    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

    # knygos galutinis adresas
    def get_absolute_url(self):
        return reverse('bookdetail', args=[str(self.id)])

    # knygos trynimas
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)


class Author(models.Model):
    first_name = models.CharField('Vardas', max_length=50, null=True, blank=True)
    last_name = models.CharField('Pavardė', max_length=50)
    biography = models.TextField('Biografija', max_length=5000, null=True, blank=True)
    author_photo = models.ImageField('Nuotrauka', max_length=50, upload_to='authors/Photo/', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def display_books(self):
        return ', '.join(book.title for book in self.books.all())


class BookReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    book = models.ForeignKey('Book', null=True, on_delete=models.SET_NULL, related_name='book_reviews')
    comentReview = models.TextField('Rašyti komentarą', max_length=500, null=True, blank=True)
    pdfReview = models.FileField('Įkelti recenzijos failą', upload_to='books/reviews/', null=True, blank=True)
    review_date = models.DateTimeField('Įrašo data', auto_now_add=True, )

    def __str__(self):
        return f'{self.comentReview} {self.pdfReview}'

    class Meta:
        ordering = ['review_date']

    # recenzijos galutinis adresas
    def get_absolute_url(self):
        return reverse('review-detail', args=[str(self.id)])

