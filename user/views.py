from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import CustomUserCreationForm
# Create your views here.


def loginUser(request):

    page = 'login'

    if request.method == 'POST':
        # print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print('username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('projects')
        else:
            print('Username or password is not correct')


    return render(request, 'user/login_register.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    page ='register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect('projects')
        else:
            messages.success(request, 'An error has occured during registratiom')
            

    context = {'page': page, 'form':form}
    return render(request, 'user/login_register.html', context)


def profiles(request):
    return render(request, 'user/profiles.html')