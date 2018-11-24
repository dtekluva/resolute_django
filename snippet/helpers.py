from geopy.geocoders import Nominatim



def get_address(lat, lng):
    print('-------------------',lat,lng)
    try:
        geolocator = Nominatim(user_agent="specify_your_app_name_here")
        string_= '%s,%s' %(lat,lng,)
        # location = geolocator.reverse("52.509669, 13.376294")
        location = geolocator.reverse(string_)
        print('-------------------',location.raw)
        address = location.address
        print('-----------------------',address)

        if address is None:
            raise Exception()
        
    except:
        address = "Sorry Unable To Collect Google Location At The Moment"
    
    return (address)