import django_filters
from . models import BookReview


# https://django-filter.readthedocs.io/en/stable/ref/filterset.html


class BookReviewFilter(django_filters.FilterSet):
    class Meta:
        model = BookReview
        fields = ['user', 'book']


