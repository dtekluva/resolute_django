from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from useraccounts.forms import LoginForm
from django.contrib.auth.models import User
from useraccounts.models import UserAccount
from main.models import Farmland
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
import json
from snippet import helpers
import ast

# from main.views import index
# Create your views here.

# def signUpView(request):
#     pass
#     #return HttpResponse("You are at, The api module")

def loginView(request):
    form = LoginForm()
    print(form)
    if request.method == 'POST':
        # print(request.POST)
        form = LoginForm(request.POST)
  
        if True:

            email    = request.POST.get("email", "")
            email = (email.lower())
            password    = request.POST.get("password", "")

            try:
                #GET CORRESPONDING USERNAME FROM EMAIL POSTED
                username = User.objects.get(email = email).username
                print(username)
                user = authenticate(username = username.lower(), password = password)

                user = User.objects.get(username=username)
                if (user.username == username): #allows user to login using username
                        # No backend authenticated the credentials
       
                        user = User.objects.get(username=username)
                        login(request, user)
                        return HttpResponseRedirect("../")
            except:
                return render(request, 'resolute/registration/login.html', {'form' : form, 'error':'Sorry incorrect Username or Password !!!'})
        else:
            form = LoginForm()

            return render(request, 'resolute/registration/login.html', {'form' : form})

    return render(request, 'resolute/registration/login.html', {'form' : form})

def user(request):
    page = 'user'
    users =  User.objects.all()
    person = User.objects.get(id = 1)
    print(person.useraccount.phone)
    print(users)
    return render(request, 'resolute/registration/user.html', {'page':page,
                                                                'users':users})

def create_user(request):
    exempted_fields = ["address", "password", "agency"]
    cleaned_form = helpers.clean(request.POST, exempted_fields)
    print(cleaned_form)
    try:
        if request.method == "POST" and request.user.is_superuser:
            fname = cleaned_form['first_name']
            lname = cleaned_form['last_name']
            email = cleaned_form['email']
            phone = cleaned_form['phone']
            address = cleaned_form['address']
            agency = cleaned_form['agency']
            password = cleaned_form['password']
            username = fname + agency + phone[6:]
            print(username)
            new_user = User(first_name = fname, last_name = lname, email = email, username = username)

            new_user.save()

            new_useraccount = UserAccount(  phone = phone
                                            , address = address, user_id = new_user.id, agency = agency )
            new_useraccount.save()

            new_user.set_password(password)

            return HttpResponse(json.dumps({"response":"success"}))
    
    except:
        return HttpResponse(json.dumps({"response":"fail"}))



#handle mobile auth and activity

@csrf_exempt
def mobile_register(request):

    if request.method == 'POST':

        exempted_fields = ["comunity", "full_name"]
        print(json.loads(request.body))
        cleaned_form = helpers.clean(json.loads(request.body), exempted_fields) #Load Response jason from Post and clean values remove trailing spaces
        fname = cleaned_form['full_name']
        phone = cleaned_form['phone']
        print(cleaned_form)
        community = cleaned_form['community']
        pin = cleaned_form['pin']
        username = phone

        new_user = User(first_name = fname, username = username)

        new_user.save()

        new_farm = Farmland(  phone = phone, full_name = fname
                                        , community = community, user_id = new_user.id)
        new_farm.save()

        new_user.set_password(pin + "????")
        new_user.save()


        return HttpResponse(json.dumps({"response":"success"}))

    return HttpResponse(json.dumps({"response":"failed"}))

@csrf_exempt
def mobile_signin(request):
    if request.method == 'POST':
        # print(request.POST)
        form = LoginForm(request.POST)
  
        if True:

            phone = request.POST.get("phone", "")
            password = request.POST.get("pin", "")

            try:
                #GET CORRESPONDING USERNAME FROM PHONE  NUMBER POSTED
                username = User.objects.get(username = phone).username
                print(username)
                user = authenticate(username = username.lower(), password = password + "????")

                user = User.objects.get(username=username)
                if (user.username == username): #allows user to login using username
                        # No backend authenticated the credentials
       
                        user = User.objects.get(username=username)
                        login(request, user)
                        return HttpResponse(json.dumps({"response":"success"}))
            except:
                return HttpResponse(json.dumps({"response":"failed"}))

def test(request):
    print(request.user)
    if request.user.is_authenticated:
        print('yeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeees')
    return HttpResponse(json.dumps({"response":"failed"}))


# def forgotPasswordView(request):
#     pass
#     #return HttpResponse("You are at, The api module")

# def resetpasswordView(request):
#     pass
#     #return HttpResponse("You are at, The api module")

# def register(request):
#     form = UserAccountForm()
#     if request.method == 'POST':
#         form = UserAccountForm(request.POST)
#         print("request was post-----------")
#         if form.is_valid():
#             print("form was valid-----------")
#             userObj     = form.cleaned_data
#             username    = userObj['username']
#             email       =  userObj['email']
#             password    =  userObj['password']
#             print(userObj)
#             if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):

#                 User.objects.create_user(username, email, password)
#                 user = authenticate(username = username, password = password)
#                 login(request, user)
#                 print("login user data-----------")
#                 user = User.objects.get(username=username)
#                 return index(request)

#             else:
#                 # raise form.ValidationError('Looks like a username with that email or password already exists')
#                 print("Looks like a username with that email or password already exists")
#     else:
#         form = UserAccountForm()

#     return render(request, 'user/auth_login.html', {'form' : form})