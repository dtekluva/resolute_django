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
# from rest_framework import serializers
# Create your views here.

host = 'http://localhost:8000/'

def main(request):
    # print(request.body)
    herdsman = Herdsman.objects.all()
    return render(request, 'resolute/skin-compact.html', {"herdsman":herdsman})

@csrf_exempt
def locationpost(request):
# Create your views here.
    
    # print(request.body)
    if request.method == 'POST':    

        reqPOST = (json.loads(request.body))
        raw_time = str(datetime.datetime.now())
        cleaned_json_post = dict(reqPOST['resource'][0])
        clean_time = raw_time[:18]

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
            herdsman = Herdsman.objects.get(userid = devid)

            new_location = Location(herdsman = herdsman, lat = lat, lng = lng, speed = speed, )
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


# def check(request, slug):

#     customer = Customer.objects.get(slug = slug) #for filtering get just one customer 
#     customers = Customer.objects.filter(slug = slug) # for iteration
#     locations = serializers.serialize("json", list(chain(Location.objects.filter(customer_id = customer.id)[:40], customers)) )



#     return HttpResponse(locations)



# def track(request, slug):

#     return render(request, 'resolute/tracking.html', {"slug":slug})

# def test(request):

#     return render(request, 'resolute/test.html')

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