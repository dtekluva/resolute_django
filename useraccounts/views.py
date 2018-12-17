from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from useraccounts.forms import LoginForm
from django.contrib.auth.models import User
from useraccounts.models import UserAccount, Token_man, Session
from main.models import Farmland
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from snippet import helpers
import ast


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
        users =  User.objects.filter(is_staff = True)
        person = User.objects.get(id = 1)
        print(person.useraccount.phone)
        print(users)
        return render(request, 'resolute/registration/user.html', {'page':page,
                                                                'users':users})

def get_users(request):
        user_list = []
        data = 0
        users =  UserAccount.objects.filter(user__is_staff = True).order_by('-id')[0:1]
        for user in users:
                data = {
                        'id':user.user_id, 
                        'first_name':user.user.first_name, 
                        'last_name':user.user.last_name, 
                        'email':user.user.email, 
                        'phone':user.phone, 
                        'agency':user.agency
                        }
                user_list.append(data)

        response = json.dumps(user_list)

        return HttpResponse(response)


def create_user(request):
        exempted_fields = ["address", "password", "agency"]
        cleaned_form = helpers.clean(request.POST, exempted_fields)

        try:
                if request.method == "POST" and request.user.is_superuser:
                        fname = cleaned_form['first_name']
                        lname = cleaned_form['last_name']
                        email = cleaned_form['email']
                        phone = cleaned_form['phone']
                        address = cleaned_form['address']
                        agency = cleaned_form['agency']
                        password = cleaned_form['password']
                        username = "".join(fname.split()) + "".join(agency.split()) + phone[6:]
                        print(username)
                        new_user = User(first_name = fname, last_name = lname, email = email, username = username, is_staff = True)

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

        #Load Response jason from Post and clean values remove trailing spaces
        cleaned_form = helpers.clean(json.loads(request.body), exempted_fields) 

        fname = cleaned_form['full_name']
        phone = cleaned_form['phone']
        community = cleaned_form['community']
        pin = cleaned_form['pin']
        username = phone

        if User.objects.filter(username = username).count() > 0:
                return HttpResponse(json.dumps({"response":"failed", 'code': '400', 'message':'Phone number exists'}))

        new_user = User(first_name = fname, username = username)

        new_user.save()

        #NEW FARM REFERS TO A NEW FARMLAND
        new_farm = Farmland(  phone = phone, full_name = fname
                                        , community = community, user_id = new_user.id)

        #add  mobile authentication token                                
        tokenize = Token_man(new_farm)
        tokenize.add_token()

        new_farm.save()

        new_user.set_password(pin + "????")
        new_user.save()


        return HttpResponse(json.dumps({"response":"success", 'auth_keys': {'client_username': new_farm.user.username, 'client_token': new_farm.token}}))

    return HttpResponse(json.dumps({"response":"failed"}))

@csrf_exempt
def mobile_signin(request):

        if request.method == 'POST':

                try:
                        post = json.loads(request.body)
                        phone = post['phone']
                        password = post['pin'] + "????"
                except:
                        return HttpResponse(json.dumps({"response":"failed", 'code':['400','Invalid Json Payload'] }))
 

                #NOTE THAT CLIENT TOKEN IS NO LONGER REQUIRED BUT JUST THERE, TO BE REMOVED AT A LATER TIME
                client_token = None

                #GET CORRESPONDING USERNAME FROM PHONE  NUMBER POSTED
                try:
                        username = User.objects.get(username = phone).username
                        user = authenticate(username = username.lower(), password = password)
                        user = User.objects.get(username=username)
                        logged_user = User.objects.get(username=phone)
                        
                        if logged_user.check_password(password) != True:
                                raise Exception('err')
                        
                except:
                        return HttpResponse(json.dumps({"response":"failed", 'code':'400', 'message':'Invalid Auth Data' }))

                if user.username == username: #allows user to login using username

                        user = User.objects.get(username=username)
                        farmland = Farmland.objects.get(user__id = user.id)
                        
                        # if not _authenticate(farmland, client_token):
                        #         return HttpResponse(json.dumps({"response":"failed", 'code':['401','unauthorized request, (Bad token)'] })) 

                        try:
                                existing_session = Session.objects.get(user__id = farmland.id, is_active = True)
                                existing_session.disable()
                        
                        except:
                                pass

                        if Session.objects.filter(user__id = farmland.id, is_active = True).count() < 1:
                                new_session = Session.objects.create(user = farmland)
                                new_session.save()
                                
                                return HttpResponse(json.dumps({"response":"success",  'auth_keys': {'session_token': new_session.token, 'client_token': farmland.token}}))

        return HttpResponse(json.dumps({"response":"failed", 'code':['400','Bad request'] }))

@csrf_exempt
def test(request):
    print(request.META['HTTP_USER_AGENT'])     
    print(request.user.is_authenticated)

    return HttpResponse(json.dumps({"response":"failed"}))

#THIS AUTHENTICATE ALSO LIES IN THE SESSION OBJECT IT HAS BEEN PUT HERE TO ALLOW FOR AUTH BEFORE CREATING A NEW SESSION
def _authenticate(_object, token):
        if _object.token == token:
                return True
        return False