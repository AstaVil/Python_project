from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from . forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from account.models import Account
from bookcase.models import Book, Author, BookReview
from taskpost.models import TaskPost
from django.core.paginator import Paginator
from django.db.models import Q

def account_view(request):
    if not request.user.is_authenticated:
        return redirect('home')
    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountUpdateForm(
				initial= {
                    'email': request.user.email,
					'username': request.user.username,
				}
			)
    context['account_form'] = form
    return render(request, 'account/account.html', context)


def accounts_list(request):
	paginator = Paginator(Account.objects.all(), 5)
	page_number = request.GET.get('page')
	paged_accounts = paginator.get_page(page_number)

	context = {
        'accounts_list': paged_accounts
    }
	return render(request, 'account/accounts_list.html', context=context)


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return render(request, 'register/welcome.html')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'register/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    context = {}

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user.is_admin or user.is_superuser:
                login(request, user)
                return redirect('dashboard')
            elif user.is_teacher:
                login(request, user)
                return redirect('teacher')
            else:
                login(request, user)
                return redirect('student')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'register/login.html', context)


# admin ir superuserio pagrindinis psl
@login_required
def dashboard(request):
    users = Account.objects.all()
    books = Book.objects.all()
    authors = Author.objects.all()
    reviews = BookReview.objects.all()
    tasks = TaskPost.objects.all()

    context = {
		'users':users,
		'books':books,
        'authors': authors,
        'reviews': reviews,
        'tasks':tasks
    }
    return render(request, 'homepages/dashboard.html', context=context)

# mokytojo pagrindinis psl
@login_required
def teacher(request):
    users = Account.objects.all()
    books = Book.objects.all()
    authors = Author.objects.all()
    reviews = BookReview.objects.all()
    tasks = TaskPost.objects.all()

    context = {
		'users':users,
		'books':books,
        'authors': authors,
        'reviews': reviews,
        'tasks':tasks
    }
    return render(request, 'homepages/teacher_home.html',context=context)

# studento pagrindinis psl
@login_required
def student(request):
    users = Account.objects.all()
    books = Book.objects.all()
    authors = Author.objects.all()
    reviews = BookReview.objects.all()
    tasks = TaskPost.objects.all()

    context = {
		'users':users,
		'books':books,
        'authors': authors,
        'reviews': reviews,
        'tasks': tasks
    }
    return render(request, 'homepages/student_home.html', context=context)


