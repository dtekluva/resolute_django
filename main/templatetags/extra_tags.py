from django import template

register = template.Library()


@register.filter(name='lead_zero')
def lead_zero(value, desired_digits):
    """NOTE THAT IT IS ASSUMED THE TWO VALUES COMING IN AS PARAMETERS @value and @desired_digits
    ARE INTEGERS"""
    if str(value).startswith("2"): #CHECK IF ITS A '234' FORMAT NUMBER, IF SO JUST RETURN THE NUMBER 
        return value
    elif str(value).startswith("0"): #CHECK IF ITS A '0...' FORMAT NUMBER AND ALSO WAS KEPT IN SAID FORMAT.
        return value
    else:
        return str(value).zfill(len(str(value))+1) #IF IT IS A '080' NUMBER THEN PAD IT WITH ON ZERO BASED ON THE LENGTH OF THE THE VALUE, THAT IS WHY IT IS FIRST CONVERTED TO A STRING AND THEN WE GET THE LENGTH OF IT AFTER.

@register.filter(name='replace_state')
def replace_state(text): 

    #This template tag replaces strings in the template in this case to replace the string "state" in the profile page.

    if "state" in text.lower():
        text = text.lower().replace("state", "")
    

    return text