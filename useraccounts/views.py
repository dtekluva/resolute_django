from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from useraccounts.forms import UserAccountForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import json
# from main.views import index
# Create your views here.

# def signUpView(request):
#     pass
#     #return HttpResponse("You are at, The api module")

def loginView(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(request.POST)
        # print("---------------------request was post-----------")
        # print(request.POST.get("username", ""))
        # if form.is_valid():
        if True:
            # print("form was valid-----------")
            # userObj     = form.cleaned_data()
            username    = request.POST.get("username", "")
            username = (username.lower())
            password    = request.POST.get("password", "")
            # print(username, password)
            user = authenticate(username = username.lower(), password = password)
            try:
                user = User.objects.get(username=user)
                if (user.username == username): #allows user to login using username
                        # No backend authenticated the credentials
                        # print(username)
                        user = User.objects.get(username=username)
                        login(request, user)
                        return HttpResponseRedirect("../")
            except:
                return render(request, 'registration/login.html', {'form' : form, 'error':'Sorry incorrect Username or Password !!!'})
        else:
            form = LoginForm()

            return render(request, 'registration/login.html', {'form' : form})

    return render(request, 'registration/login.html', {'form' : form})

def forgotPasswordView(request):
    pass
    #return HttpResponse("You are at, The api module")

def resetpasswordView(request):
    pass
    #return HttpResponse("You are at, The api module")

def register(request):
    form = UserAccountForm()
    if request.method == 'POST':
        form = UserAccountForm(request.POST)
        print("request was post-----------")
        if form.is_valid():
            print("form was valid-----------")
            userObj     = form.cleaned_data
            username    = userObj['username']
            email       =  userObj['email']
            password    =  userObj['password']
            print(userObj)
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):

                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                print("login user data-----------")
                user = User.objects.get(username=username)
                return index(request)

            else:
                # raise form.ValidationError('Looks like a username with that email or password already exists')
                print("Looks like a username with that email or password already exists")
    else:
        form = UserAccountForm()

    return render(request, 'user/auth_login.html', {'form' : form})