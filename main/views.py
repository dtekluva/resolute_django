from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import User, Herdsman, Bounds, Location, Farmland, Collection, Incident
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
    incidents = Incident.objects.all().count()
    herdsmen = Herdsman.objects.all().count()
    farmers = Farmland.objects.all().count()
    states = Herdsman.objects.values_list('state', flat=True).count()#get unique states from herdsmen object
    # print(herdsmen, farmers, states)
    page = 'index'
    return render(request, 'resolute/main/index.html', {'posts':collections, 'page': page, 'total_farmers': farmers, 'total_states': states, 'total_herdsmen':herdsmen, 'incidents':incidents})


def detail_view(request):

    herdsman = Herdsman.objects.all()

    return render(request, 'resolute/skin-compact.html', {"herdsman":herdsman})

@login_required
def table(request):

    locations = Location.objects.all().order_by('-date')
    page = 'table'
    return render(request, 'resolute/main/table.html', {'posts':locations, 'page': page})

@csrf_exempt
def incidents(request):

    incidents = Incident.objects.all().order_by('-id')
    page = 'incidents'

    return render(request, 'resolute/main/incident.html', {'page': page, 'incidents':incidents})


@csrf_exempt
def farmers(request):

    farmers = Farmland.objects.all().order_by('-id')
    page = 'farmers'

    return render(request, 'resolute/main/farmers.html', {'page': page, 'farmers':farmers})


@csrf_exempt
def herdsmen(request):

    herdsmen = Herdsman.objects.all().order_by('-id')
    page = 'herdsmen'

    return render(request, 'resolute/main/herdsmen.html', {'page': page, 'herdsmen':herdsmen})



@csrf_exempt
def locationpost(request):
# Create your views here.
    print(request.body)
    tz = pytz.timezone('Africa/Lagos')
    lagos = datetime.now(tz)
    formatedDate = lagos.strftime("%Y-%m-%d %H:%M:%S")

    if request.method == 'POST':
        # print('carrying out test')
        try:
            reqPOST = (json.loads(request.body))
            cleaned_json_post = dict(reqPOST['resource'][0])
        except:
            reqPOST = json.loads(ast.literal_eval(str(request.body).replace('\\', '')))
            cleaned_json_post = dict(reqPOST['resource'][0])

        devid = cleaned_json_post["devid"]
        time  = cleaned_json_post["time"]
        etype = cleaned_json_post["etype"]
        engine = cleaned_json_post["engine"]
        lat = cleaned_json_post["lat"]
        lng = cleaned_json_post["lon"]
        vbat = cleaned_json_post["vbat"]
        speed = cleaned_json_post["speed"][0:4]
        pint = cleaned_json_post["pInt"]


        if lat != '0' and lng != '0' :
            clean_address = helpers.get_address(lat,lng)
            address = clean_address['address']
            state = clean_address['state']
            try:
                #GET CORRESPONDING HERDSMAN OBJECT
                herdsman = Herdsman.objects.get(userid = devid)
                herdsman.lng = lng
                herdsman.lat = lat
                herdsman.state = state
                herdsman.address = address
                herdsman.save()
                last_location_post = Location.objects.filter(herdsman = herdsman).order_by('-id')[0]

            except:
                return HttpResponse(json.dumps('No user with id {} found in data base please confirm'.format(devid)))#GET LAST LOCATION FOR TIME COMPARISM


            if post_is_too_old(lagos, last_location_post): #CHECK IF INTERVAL NOT EXCEEDED
                last_collection = Collection(herdsman = herdsman, start = formatedDate, lng = lng, lat = lat) #CREATE A NEW COLLECTION IF INTERVAL EXCEEDED

                last_collection.save()

            else: #SKIP FILTERING OF LAST COLLECTION IF WE CREATED NEW, SINCE WE HAVE THE VALUE ALREADY

                last_collection = Collection.objects.filter(herdsman = herdsman.id).order_by('-id')[0] #GET MOST RECENT COLLECTION

            #CREATE NEW LOCATION OBJECT
            new_location = Location(state = state, collection = last_collection, herdsman = herdsman, lat = lat, lng = lng, speed = speed, address = address, date = formatedDate)
            new_location.save()


            last_collection.lat, last_collection.lng= [lat,lng] #UPDATE COLLECTION LATITUDE AND LONGITUDE
            last_collection.stop = new_location.date #UPDATE COLLECTION STOP TIME
            last_collection.save()



            return HttpResponse(json.dumps('Added post to device id {}, name {} '.format(devid, herdsman.name)))

    return HttpResponse(json.dumps({'Success' : 'success'}))


def post_is_too_old(new_post_time, old_post):
    lastlocation = old_post
    last_post_in_seconds = lastlocation.date.timestamp()

    time_difference = (new_post_time.timestamp() - last_post_in_seconds)/60  #CONVERT SECONDS TO MINUTES

    if time_difference > settings.POSTINTERVAL :
        return True
    else :
        return False


def check(request, slug):

    herdsman = Herdsman.objects.get(slug = slug) #for filtering get just one customer
    herdsmen = Herdsman.objects.filter(slug = slug) # for iteration
    locations = serializers.serialize("json", list(chain(Location.objects.filter(herdsman_id = herdsman.id).order_by('id'), herdsmen)) )

    return HttpResponse(locations)

def get_lat_lng(request, id):

    try:
        target = Herdsman.objects.get(id = id) #for filtering get just one customer
        lat = target.lat
        lng = target.lng

        name = target.name
        # print(name)

    except:
        target = Farmland.objects.get(id = id) #for filtering get just one customer
        lat = target.lat
        lng = target.lng

    return HttpResponse(json.dumps({'lat':lat, 'lng':lng}))

def collection_check(request, id):

    collection = Collection.objects.get(id = id)
    herdsman = Herdsman.objects.get(id = collection.herdsman.id) #for filtering get just one customer
    herdsmen = Herdsman.objects.filter(id = collection.herdsman.id) # for iteration
    locations = serializers.serialize("json", list(Location.objects.filter(collection_id = collection.id).order_by('id')))

    return HttpResponse(locations)

def check_panic(request):
    panicking_herdsmen = Herdsman.objects.filter(is_panicking = True)
    panicking_farmers = Farmland.objects.filter(is_panicking = True)

    panicking = serializers.serialize("json", list(chain(panicking_farmers, panicking_herdsmen)))

    return HttpResponse(panicking)


#RESOLVE PANIC
@csrf_exempt
def resolve_panic(request):
    # print(request.body)
    # print(json.loads(request.body))
    response = json.loads(request.body)
    incident = Incident.objects.get(id = response['data']['incident_id'])
    user = User.objects.get(id = incident.user_id)
    incident.is_resolved = True
    incident.save()

    try:
        target = Farmland.objects.get(user_id = user.id)
        target.is_panicking = False
        target.save()

    except:
        target = Herdsman.objects.get(user_id = user.id)
        target.is_panicking = False
        target.save()

    return HttpResponse(json.dumps(response))

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
    # # print(c)
    # 0.0009 = "100m"
    # 0.009 = "1km"
    if c >= 0.00001:
        return True

    else:
        return False

#HANDLE BOUNDS POST FROM MOBILE

def get_latlng(request, username):
    bounds_list = []
    try:
        user = User.objects.get(username = username)
        farmland = Farmland.objects.get(user = user.id)
        bounds = Bounds.objects.filter(farmland = farmland)

        # print(len(bounds))
        for location in bounds:

            point = [location.lat, location.lng]
            bounds_list.append(point)

        start_latlng = [bounds[0].lat, bounds[0].lng]
        end_latlng = [bounds[len(bounds)-1].lat, bounds[len(bounds)-1].lng]

        response = {"response":"success","data":{"bounds":bounds_list, "start_latlng":start_latlng, "end_latlng":end_latlng}, 'message': 'user {}'.format(farmland), }

        return HttpResponse(json.dumps(response))

    except :
        response = {"response":"Failed","data":bounds_list, "message": "user not found" }

        return HttpResponse(json.dumps(response))


@csrf_exempt
#POST LAT_LNG SERIES FOR BOUNDS PURPOSES DIFFERENT FROM PANIC
def post_latlng(request):
    new_request = json.loads(request.body)
    username = new_request['username']
    auth_data = new_request['auth']

    try:
        user = User.objects.get(username = username)
        farmland = Farmland.objects.get(user = user.id)
        farmland.is_mapped = True
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

                #SAVE FARMLAND IS_MAPPED SINCE ALL PROCESSES OF ADDING BOUNDS WERE SUCCESSFUL
                farmland.save()
            return HttpResponse(json.dumps({"response":"success", "message": "Added bound to {}".format(farmland.user),  'auth_keys': {'session_token': session.token}}))
    except:
        return HttpResponse(json.dumps({"response":"failed", 'code':'401', 'message':'unauthorized request, (Bad token)' }))

@csrf_exempt
def create_panic(request):
    new_request = json.loads(request.body)
    username    = new_request['data']['username']
    auth_data   = new_request['auth']
    data        = new_request['data']
    user_type    = new_request['user_type']
    user_type2    = new_request['user_type']

    try:
        if user_type == "farmer" or user_type2 == "farmer":
            user = User.objects.get(username = username)
            # print(user)
            logged_user =Farmland.objects.get(user = user.id)
            session  = Session.objects.get(token = auth_data['session_token'], is_active = True)

            if session._authenticate(auth_data):

                    logged_user.lat, logged_user.lng = data['lat'], data['lng'] # ADD USER LOCATION OF FARMER TO THE FARMLAND
                    logged_user.is_panicking = True
                    logged_user.save()

                    #CREATE NEW PANIC INCIDENT
                    new_incident = Incident(user =logged_user.user, details = data['details'], lat = data['lat'], lng = data['lng'], name =logged_user.full_name, is_farmer = True, location =logged_user.community)
                    new_incident.save()

                    return HttpResponse(json.dumps({"response":"success", "message": "{} is now panicking".format(logged_user.user),  'auth_keys': {'session_token': session.token}}))

        elif user_type == "herdsman" or user_type == "herdsman":
            user = User.objects.get(username = username)
            # print(user)
            logged_user =Herdsman.objects.get(user = user.id)
            session  = Session.objects.get(token = auth_data['session_token'], is_active = True)

            if session._authenticate(auth_data):

                    logged_user.lat, logged_user.lng = data['lat'], data['lng'] # ADD USER LOCATION OF FARMER TO THE FARMLAND
                    logged_user.is_panicking = True
                    logged_user.save()

                    #CREATE NEW PANIC INCIDENT
                    new_incident = Incident(user =logged_user.user, details = data['details'], lat = data['lat'], lng = data['lng'], name ="{} {}".format(logged_user.name, logged_user.surname ) , is_herdsman= True, location =logged_user.address)
                    new_incident.save()

                    return HttpResponse(json.dumps({"response":"success", "message": "{} is now panicking".format(logged_user.user),  'auth_keys': {'session_token': session.token}}))


    except :

        return HttpResponse(json.dumps({"response":"failed", 'code':'401', 'message':'unauthorized request, (Bad token)' }))

def resolve_panic_mobile():
    pass

@csrf_exempt
def get_client_data(request):

    new_request = json.loads(request.body)
    username = new_request['data']['username']
    auth_data = new_request['auth']
    user_type = new_request['user_type']

    user = User.objects.get(username = username)
    session  = Session.objects.get(token = auth_data['session_token'], is_active = True)

    if session._authenticate(auth_data):

            if user_type == "farmer":

                farmland = Farmland.objects.get(user = user.id)


                return HttpResponse(json.dumps({"response":"success", "data": {"name":farmland.full_name, "phone":farmland.phone, "address":farmland.community},  'auth_keys': {'session_token': session.token}}))

            if user_type == "herdsman":

                herdsman = Herdsman.objects.get(user = user.id)


                return HttpResponse(json.dumps({"response":"success", "data": {"name":(herdsman.name +" "+ herdsman.surname), "phone":herdsman.phone, "address":herdsman.address, "no_cattle":herdsman.no_of_cattle},  'auth_keys': {'session_token': session.token}}))



    return HttpResponse(json.dumps({"response":"failed", 'code':'401', 'message':'unauthorized request, (Bad token)' }))


@csrf_exempt
def recurring_gps_post(request):

    new_request = json.loads(request.body)
    username = new_request['data']['username']
    lat = new_request['data']['lat']
    lng = new_request['data']['lng']
    auth_data = new_request['auth']
    user_type = new_request['user_type']

    user = User.objects.get(username = username)
    session  = Session.objects.get(token = auth_data['session_token'], is_active = True)

    if session._authenticate(auth_data):

            if user_type == "farmer":

                farmland = Farmland.objects.get(user = user.id)
                farmland.lat = lat
                farmland.lng = lng
                farmland.save()

                return HttpResponse(json.dumps({"response":"success", "data": {"name":farmland.full_name, "phone":farmland.phone, "address":farmland.community},  'auth_keys': {'session_token': session.token}}))

            if user_type == "herdsman":

                herdsman = Herdsman.objects.get(user = user.id)
                herdsmnan.lat = lat
                herdsmnan.lng = lng
                herdsmnan.save()


                return HttpResponse(json.dumps({"response":"success", "data": {"name":(herdsman.name +" "+ herdsman.surname), "phone":herdsman.phone, "address":herdsman.address, "no_cattle":herdsman.no_of_cattle},  'auth_keys': {'session_token': session.token}}))



    return HttpResponse(json.dumps({"response":"failed", 'code':'401', 'message':'unauthorized request, (Bad token)' }))



def profile_page(request, target_id, is_farmer):

    user_type  = 'farmer' if eval(is_farmer)  else 'herdsman'

    if user_type == 'herdsman' :

        user = User.objects.get(incident = target_id)
        collection = Herdsman.objects.get(user = user.id)
        # print(collection.name)

    elif user_type == 'farmer' :

        user = User.objects.get(incident = target_id)
        collection = Farmland.objects.get(user = user.id)

    page = 'profile'

    return render(request, 'resolute/main/profile.html', {'page': page, 'user_type':user_type, 'collection':collection})