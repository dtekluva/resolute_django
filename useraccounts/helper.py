from main.models import Positions, Incident
from useraccounts.models import UserAccount
from snippet import Client

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
    print("REACHED HERE ATLAST WOOHOO")
    recipients_list = UserAccount.objects.all()
 
    message = f"{panic_name} of {panic_location} just pushed a panic alert. \nCall: {panic_phone}.\n\nSee location: http://www.google.com/maps/place/{panic_position.lat},{panic_position.lng}"


    account_key = '533627b3' 
    secret = 'ckLc6G8YwK2oBhAl' 
    client = Client(key=account_key, secret=secret)

    for recipient in recipients_list:

        recipient = "234" + (recipient.phone)[1:] if len(recipient.phone) < 12 else recipient.phone

        responseData = client.send_message(
            {
                "from": "RESOLUTE",
                "to": recipient,
                "text": message
            }
        )

        if responseData["messages"][0]["status"] == "0":
            print(f"Message sent to {recipient} successfully.")
        else:
            print(f"Message failed with error: {responseData['messages'][0]['error-text']}")