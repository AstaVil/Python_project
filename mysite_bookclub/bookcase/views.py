from django.conf import settings
from account.models import Account
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from . models import Book, Author, BookReview
from . forms import AuthorUploadForm, BookUploadForm, BookReviewForm
from . filters import BookReviewFilter





def homeScreenView(request):
	books = Book.objects.all()
	context = {
		'books':books,
	}
	return render(request, "index.html", context)

# ___________________________________________________________
# autoriaus views:

def authors_list(request):
	paginator = Paginator(Author.objects.all(), 9)
	page_number = request.GET.get('page')
	paged_authors = paginator.get_page(page_number)
	context = {
        'authors': paged_authors
    }
	return render(request, 'bookcase/authors_list.html', context=context)

def upload_author(request):
	if request.method == 'POST':
		form = AuthorUploadForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('upload_book')
	else:
		form = AuthorUploadForm()
	context = {
        'form': form
    }
	return render(request, 'bookcase/upload_author.html',context )

def get_author(request, id):
	author = get_object_or_404(Author, id=id)
	book = Book.objects.filter(author_id=author.id)
	context = {
        'author': author,
        'book': book
    }
	return render(request, "bookcase/author.html", context)

# ________________________________________________________________________
#  knygu views:

def books_list(request):
	paginator = Paginator(Book.objects.all(), 9)
	page_number = request.GET.get('page')
	paged_books = paginator.get_page(page_number)
	context = {
        'books_list': paged_books
    }
	return render(request, 'bookcase/books_list.html', context)


def upload_book(request):
	if request.method == 'POST':
		form = BookUploadForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('books_list')
	else:
		form = BookUploadForm()
	context = {
        'form': form
    }
	return render(request, 'bookcase/upload_book.html',context )


def delete_book(request, id):
	if request.method == 'POST':
		book = Book.objects.get(id=id)
		book.delete()
	return redirect('books_list')


def search_book(request):
	query = request.GET.get('query')
	lt_letters = {'ą':'a','č':'c','ę':'e','ė':'e','į':'i','š':'s','ų':'u','ū':'u','ž':'z'}
	for raide in query:
		if raide in lt_letters.keys():
			print(lt_letters[raide])
	search_results = Book.objects.filter(Q(title__icontains=query) | Q(desc__icontains = query))
	context = {
		'search_results': search_results,
		'query': query
	}

	return render(request, 'bookcase/search_book.html', context)


@login_required
def get_book(request, id):
	book = get_object_or_404(Book, id=id)

	onebook_reviews = BookReview.objects.filter(book_id=id).order_by('-review_date')
	onebook_reviews_count = onebook_reviews.count()

	paginator = Paginator(onebook_reviews, 4)
	page_number = request.GET.get('page')
	paged_reviews = paginator.get_page(page_number)

	context = {
        'book': book,
		'onebook_reviews': paged_reviews,
		'onebook_reviews_count': onebook_reviews_count
	}
	return render(request, "bookcase/bookdetail.html", context)

# ________________________________________________________________________
# recenzijų views
def reviews_list(request):
	reviews_list = BookReview.objects.all().order_by('-review_date')
	all_reviews_count = reviews_list.count()
	rev_filter = BookReviewFilter(request.GET, queryset=reviews_list)
	reviews_list = rev_filter.qs

	context = {
        'reviews_list': reviews_list,
		'all_reviews_count': all_reviews_count,
		'rev_filter': rev_filter
    }
	return render(request, 'reviews/reviews_list.html', context)


@login_required
def send_review(request):
	if request.method == 'POST':
		form = BookReviewForm(request.POST, request.FILES)
		if form.is_valid():
			review = form.save(commit=False)
			review.user = request.user
			review.save()
			return render(request, 'reviews/success_rev_send.html')

	else:
		form = BookReviewForm()
	context = {
		'form': form
	}

	return render(request, 'reviews/send_review.html', context)



# _____________________________________________________________________________
# žinutė puslapis neveikia

def message_renewal(request):
	return render(request, 'fragments/message_renewal.html')



