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
        state = dict(location.raw)['address']['state']
        if address is None:
            raise Exception()
        
    except:
        address = "Sorry Unable To Collect Google Location At The Moment"
        state = "Not available"
    
    return {'address':address, 'state':state}

def clean(txt, exempt = "none"):
    """form query dict and fields to exempt from cleaning, returns form values 
        without spaces upgrade later to remove special chars"""

    new_dict = {}
    for key in txt:
        new_dict[key] = ((txt[key]).strip())
        if key not in exempt:
            new_dict[key] = (new_dict[key]).replace(" ","").lower()
    return new_dict


def format_date(date):
    "**Change date format for django**"
    date = date.split("/")

    return (date[2]+"-"+date[1]+"-"+date[0])

