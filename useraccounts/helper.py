from main.models import Positions, Incident
from useraccounts.models import UserAccount
import requests

def create_dummy_incident(user, user_type):

    if user_type == "herdsman":
        new_incident = Incident(user = user, details = "Test", lat = 0, lng = 0, name ="null", is_herdsman = True, location ="user.null", is_active = False, is_resolved = True)

        

    elif user_type == "farmer":
        new_incident = Incident(user = user, details = "Test", lat = 0, lng = 0, name ="null", is_farmer = True, location ="null", is_active = False, is_resolved = True)


    new_incident.save()
    return new_incident

def create_dummy_position(user, incident, user_type):

    if user_type == "herdsman":
        new_position = Positions(user = user, incident = incident, details = "Test", lat = 0, lng = 0, name ="null", is_herdsman = True, location ="user.null", is_active = False, is_resolved = True)
    
    elif user_type == "farmer":
        new_position = Positions(user = user, incident = incident, details = "Test", lat = 0, lng = 0, name ="null", is_farmer = True, location ="null", is_active = False, is_resolved = True)


    new_position.save()


def alert_security(panic_name, panic_location, panic_phone, panic_position):
    recipients_list = UserAccount.objects.all()
 
    text = ""
    for recipient in recipients_list:
        text += f"{recipient.phone},"

    recipients = text[:-1]

    username = "joseph@univelcity.com"
    api_key = "d5f6b1f22da4663d6983a93ffabaedca4b8c78d0"
    sender  = "RESOLUTE"

    message = f"{panic_name} of {panic_location} just pushed a panic alert. \nCall: {panic_phone}.\n\nSee location: http://www.google.com/maps/place/{panic_position.lat},{panic_position.lng}"


    url = f"http://api.ebulksms.com:8080/sendsms?username={username}&apikey={api_key}&sender={sender}&messagetext={message}&flash=0&recipients={recipients}"

    response = requests.get(url)

    print(response.text, recipients)
    print(message)