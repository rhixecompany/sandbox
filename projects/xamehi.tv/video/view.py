from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import *
from .decorators import *
from .forms import MoviesForm, SeriesForm,  CustomUserCreationForm, ProfileForm, UserForm
from .filters import MoviesFilter, SeriesFilter


# Create your views here.


def index(request):
    movies = Movies.objects.filter(active=True, featured=True)[0:3]
    context = {'movies': movies}
    return render(request, 'video/index.html', context)


def movies(request):
    movies = Movies.objects.filter(active=True)
    myFilter = MoviesFilter(request.GET, queryset=movies)
    movies = myFilter.qs
    page = request.GET.get('page')
    paginator = Paginator(movies, 5)

    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    context = {'movies': movies, 'myFilter': myFilter}
    return render(request, 'video/movies.html', context)


def movie(request, slug):
    movie = Movies.objects.get(slug=slug)

    if request.method == 'POST':
        MoviesComment.objects.create(
            author=request.user.profile,
            movie=movie,
            body=request.POST['comment']
        )
        messages.success(request, "You're comment was successfuly posted!")

        return redirect('movie', slug=movie.slug)

    context = {'movie': movie}
    return render(request, 'video/movie.html', context)


def sendEmail(request):

    if request.method == 'POST':

        template = render_to_string('video/email_template.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['admin@xamehi.tv']
        )

        email.fail_silently = False
        email.send()

    return render(request, 'video/email_sent.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Little Hack to work around re-building the usermodel
        try:
            user = User.objects.get(email=email)
            user = authenticate(
                request, username=user.username, password=password)
        except:
            messages.error(request, 'User with this email does not exists')
            return redirect('login')

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Email OR password is incorrect')

    context = {}
    return render(request, 'video/login.html', context)


def registerPage(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Account successfuly created!')

            user = authenticate(request, username=user.username,
                                password=request.POST['password1'])

            if user is not None:
                login(request, user)

            next_url = request.GET.get('next')
            if next_url == '' or next_url == None:
                next_url = 'index'
            return redirect(next_url)
        else:
            messages.error(request, 'An error has occured with registration')
    context = {'form': form}
    return render(request, 'video/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('index')

# CRUD VIEWS


@admin_only
@login_required(login_url="index")
def createMovie(request):
    form = MoviesForm()

    if request.method == 'POST':
        form = MoviesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('movies')

    context = {'form': form}
    return render(request, 'video/movie_form.html', context)


@admin_only
@login_required(login_url="index")
def updateMovie(request, slug):
    movie = Movies.objects.get(slug=slug)
    form = MoviesForm(instance=movie)

    if request.method == 'POST':
        form = MoviesForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
        return redirect('movies')

    context = {'form': form}
    return render(request, 'video/movie_form.html', context)


@admin_only
@login_required(login_url="index")
def deleteMovie(request, slug):
    movie = Movies.objects.get(slug=slug)

    if request.method == 'POST':
        movie.delete()
        return redirect('movies')
    context = {'item': movie}
    return render(request, 'video/delete.html', context)


@login_required(login_url="index")
def userAccount(request):
    profile = request.user.profile

    context = {'profile': profile}
    return render(request, 'video/account.html', context)


@login_required(login_url="index")
def updateProfile(request):
    user = request.user
    profile = user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()

        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'video/profile_form.html', context)
