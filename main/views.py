from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import User, Herdsman, Bounds, Location, Farmland, Collection
import json, math, datetime, pytz, ast
from itertools import chain #allow for merging multiple querysets frorm different models
from django.core import serializers
from snippet import helpers
from datetime import datetime, timezone, timedelta
from django.contrib.auth.decorators import login_required, permission_required
from resolute import settings
from useraccounts.models import Session


# from rest_framework import serializers
# Create your views here.

host = 'http://localhost:8000/'

@login_required
def index(request):
    collections = Collection.objects.all().order_by('-id')[:10]
    herdsmen = Herdsman.objects.all().count()
    farmers = Farmland.objects.all().count()
    states = Herdsman.objects.values_list('state', flat=True).count()
    print(herdsmen, farmers, states)
    page = 'index'
    return render(request, 'resolute/main/index.html', {'posts':collections, 'page': page, 'total_farmers': farmers, 'total_states': states, 'total_herdsmen':herdsmen})


def detail_view(request):

    herdsman = Herdsman.objects.all()

    return render(request, 'resolute/skin-compact.html', {"herdsman":herdsman})

@login_required
def table(request):

    locations = Location.objects.all().order_by('-date')
    page = 'table'
    return render(request, 'resolute/main/table.html', {'posts':locations, 'page': page})


@csrf_exempt
def locationpost(request):
# Create your views here.
    tz = pytz.timezone('Africa/Lagos')
    lagos = datetime.now(tz)
    formatedDate = lagos.strftime("%Y-%m-%d %H:%M:%S")

    # print(request.body)
    if request.method == 'POST':    

        reqPOST = (json.loads(request.body))
        cleaned_json_post = dict(reqPOST['resource'][0])

        devid = cleaned_json_post["devid"] 
        time  = cleaned_json_post["time"]
        etype = cleaned_json_post["etype"]
        engine = cleaned_json_post["engine"]
        lat = cleaned_json_post["lat"]
        lng = cleaned_json_post["lon"]
        vbat = cleaned_json_post["vbat"]
        speed = cleaned_json_post["speed"][0:5]
        pint = cleaned_json_post["pInt"]

                
        if lat != '0' and lng != '0' :
            clean_address = helpers.get_address(lat,lng)
            address = clean_address['address']
            state = clean_address['state']

            #GET CORRESPONDING HERDSMAN OBJECT
            herdsman = Herdsman.objects.get(userid = devid)
            herdsman.lng = lng
            herdsman.lat = lat
            herdsman.state = state
            # print(state)
            herdsman.address = address
            herdsman.save()


            if post_is_too_old(lagos): #CHECK IF INTERVAL NOT EXCEEDED
                last_collection = Collection(herdsman = herdsman, start = formatedDate) #CREATE A NEW COLLECTION IF INTERVAL EXCEEDED
                last_collection.save()

            else: #SKIP FILTERING OF LAST COLLECTION IF WE CREATED NEW, SINCE WE HAVE THE VALUE ALREADY

                last_collection = Collection.objects.all().order_by('-id')[0] #GET MOST RECENT COLLECTION

            #CREATE NEW LOCATION OBJECT
            new_location = Location(state = state, collection = last_collection, herdsman = herdsman, lat = lat, lng = lng, speed = speed, address = address, date = formatedDate)
            new_location.save()

            last_collection.stop = new_location.date #COLLECTION STOP TIME
            last_collection.save()


    
        return HttpResponse(json.dumps('No user with id {} found in data base please confirm'.format(devid)))   
    

    locations = Location.objects.all() # for iteration
    # result = serializers.serialize("json", locations )


    return HttpResponse(json.dumps({'Success' : 'success'}))


def post_is_too_old(new_post_time):
    lastlocation = Location.objects.all().order_by('-id')[0]
    last_post_in_seconds = lastlocation.date.timestamp()
    
    time_difference = (new_post_time.timestamp() - last_post_in_seconds) / 60 #CONVERT SECONDS TO MINUTES
    print(time_difference)
    if time_difference > settings.POSTINTERVAL :
        return True
    else :
        return False

    
def check(request, slug):

    herdsman = Herdsman.objects.get(slug = slug) #for filtering get just one customer 
    herdsmen = Herdsman.objects.filter(slug = slug) # for iteration
    locations = serializers.serialize("json", list(chain(Location.objects.filter(herdsman_id = herdsman.id).order_by('id'), herdsmen)) )

    return HttpResponse(locations)

def collection_check(request, id):

    collection = Collection.objects.get(id = id)
    herdsman = Herdsman.objects.get(id = collection.herdsman.id) #for filtering get just one customer 
    herdsmen = Herdsman.objects.filter(id = collection.herdsman.id) # for iteration
    locations = serializers.serialize("json", list(chain(Location.objects.filter(collection_id = collection.id), herdsmen)) )

    return HttpResponse(locations)


@login_required
def track(request, slug):

    return render(request, 'resolute/realtracking.html', {"slug":slug})

@login_required
def mapping(request, slug):

    herdsman = Herdsman.objects.get(slug = slug) #for filtering get just one customer 
    page = 'map'
    
    return render(request, 'resolute/main/map.html', {"herdsman":herdsman, 'slug':slug,  'page': page})

@login_required
def trail(request, slug):

    return render(request, 'resolute/trail.html', {"slug":slug})

def check_distance(old_coord, new_coord):

    a =  old_coord[0] - new_coord[0] #lat difference as opposite
    b =  old_coord[1] - new_coord[1] #lng difference as adjacent
    c = a **2 + b **2 #hypothenus as distance between two points

    c = math.sqrt(c)
    print(c)
    # 0.0009 = "100m"
    # 0.009 = "1km"
    if c >= 0.00001:
        return True
    
    else:
        return False

def get_latlng(request, username):

    user = User.objects.get(username = username)
    farmland = Farmland.objects.get(user = user.id)
    bounds = Bounds.objects.filter(farmland = farmland)
    bounds_list = []

    for location in bounds:

        point = [location.lat, location.lng]
        bounds_list.append(point)

    response = {"data":bounds_list}

    return HttpResponse(json.dumps(response))


#HANDLE BOUNDS POST FROM MOBILE

@csrf_exempt
def post_latlng(request):
    new_request = json.loads(request.body)
    username = new_request['username']
    auth_data = new_request['auth']

    user = User.objects.get(username = username)
    farmland = Farmland.objects.get(user = user.id)
    session = Session.objects.get(token = auth_data['session_token'], is_active = True)

    if session._authenticate(auth_data):

        #REMOVE DATA FROM BOUNDS BEFORE ADDING NEW BOUNDS
        bounds = Bounds.objects.filter(farmland = farmland)
        for location in bounds:
            location.delete()

        #ADD NEW BOUNDS TO DATABASE
        for latlng in new_request['data']:
            new_bound = Bounds(farmland = farmland, lat = latlng[0], lng = latlng[1])
            new_bound.save()
        
        return HttpResponse(json.dumps({"response":"success", "data": "Added bound to {}".format(farmland.user),  'auth_keys': {'session_token': session.token}}))
    else:
        return HttpResponse(json.dumps({"response":"failed", 'code':['401','unauthorized request, (Bad token)'] })) 
