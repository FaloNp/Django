from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import *

from django.contrib.auth import login, authenticate


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def category_list(request):
    categoryList = Post.CATEGORY_LIST
    return render(request, 'blog/category_list.html', {'category_list': categoryList})


def search(request):
    if request.method == 'POST':
        searched_phrase = request.POST.get('title', '')
        # Wyszukaj posty zawierające frazę w tytule
        posts = Post.objects.filter(title__icontains=searched_phrase)
        return render(request, 'blog/post_list.html', {'posts': posts, 'searched_phrase': searched_phrase})
    return render(request, 'blog/search.html')
def sort(request):
    return render(request, 'blog/sort.html',)

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/add.html', {'form': form})




def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Po zalogowaniu przekieruj na stronę, którą chcesz
                return redirect('post_list')
            else:
                # Nieudane logowanie
                error_message = "Invalid login credentials."
        else:
            # Formularz jest nieprawidłowy
            error_message = "Invalid form data."
    else:
        form = LoginForm()
        error_message = None

    return render(request, 'blog/login.html', {'form': form, 'error_message': error_message})













def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            # Sprawdź, czy użytkownik o podanej nazwie nie istnieje już w bazie
            if not User.objects.filter(username=username).exists():
                # Sprawdź, czy hasła się zgadzają
                if form.cleaned_data['password'] == form.cleaned_data['password_repeat']:
                    # Stwórz nowego użytkownika
                    user = User.objects.create_user(username=username, password=password, email=email)
                    # Zaloguj użytkownika
                    login(request, user)
                    return redirect('post_list')
                else:
                    # Hasła się nie zgadzają
                    error_message = "Passwords do not match."
            else:
                # Użytkownik o podanej nazwie już istnieje
                error_message = "Username is already taken."
        else:
            # Formularz jest nieprawidłowy
            error_message = "Invalid form data."
    else:
        form = RegistrationForm()
        error_message = None

    return render(request, 'blog/register.html', {'form': form, 'error_message': error_message})