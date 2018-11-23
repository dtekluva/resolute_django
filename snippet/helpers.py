from geopy.geocoders import Nominatim



def get_address(lat, lng):
    
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    string_= '%s,%s' %(lat,lng,)
    # location = geolocator.reverse("52.509669, 13.376294")
    location = geolocator.reverse(string_)
    print(location.address)
    return (location.address)