from main.models import Positions, Incident

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