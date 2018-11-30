from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Herdsman, Bound, Location, Farmland
import json
from itertools import chain #allow for merging multiple querysets frorm different models
from django.core import serializers
import math
import datetime
from snippet import helpers
from datetime import datetime, timezone
import pytz
from django.contrib.auth.decorators import login_required, permission_required


# from rest_framework import serializers
# Create your views here.

host = 'http://localhost:8000/'

@login_required
def index(request):
    locations = Location.objects.all().order_by('-id')
    page = 'index'
    return render(request, 'resolute/main/index.html', {'posts':locations, 'page': page})


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
        try:        
            if lat != '0' and lng != '0' :
                clean_address = helpers.get_address(lat,lng)
                address = clean_address['address']
                state = clean_address['state']
                herdsman = Herdsman.objects.get(userid = devid)
                herdsman.lng = lng
                herdsman.lat = lat
                herdsman.state = state
                print(state)
                herdsman.address = address
                herdsman.save()
                new_location = Location(state = state, herdsman = herdsman, lat = lat, lng = lng, speed = speed, address = address, date = formatedDate)
                new_location.save()
                print(devid,time, etype, engine, lat, lng, vbat, speed)

        except:
            return HttpResponse(json.dumps('No user with id {} found in data base please confirm'.format(devid)))   
    

    locations = Location.objects.all() # for iteration
    result = serializers.serialize("json", locations )


    return HttpResponse(json.dumps({herdsman.name : result}))
    
# @csrf_exempt
# def end(request):

    
#     if request.method == 'GET':
#         post = (request.GET)
#         target = Customer.objects.get(id = post["device"])
#         target.lng = post['ln']
#         target.lat = post['lt']
#         target.address  = helpers.get_address(post['lt'],post['ln'])
#         target.is_panicking = True
#         target.panicked = datetime.datetime.now()
#         target.save()

#         new_location = Location.objects.create(lat = target.lat, lng = target.lng, address = target.address, customer_id = target.id,
#                                                 speed = post['sog'], accuracy = post['hdop'])

#         return HttpResponse(json.dumps({'success':'success', "panic_status":target.is_panicking}))

        
#     return HttpResponse('Unrecognisable request method, cannot understand')


def check(request, slug):

    herdsman = Herdsman.objects.get(slug = slug) #for filtering get just one customer 
    herdsmen = Herdsman.objects.filter(slug = slug) # for iteration
    locations = serializers.serialize("json", list(chain(Location.objects.filter(herdsman_id = herdsman.id)[:40], herdsmen)) )



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

