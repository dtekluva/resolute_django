import time
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import date
from django.db import models
from main.models import Farmland
import secrets
# Create your models here.

class UserAccount(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'useraccount')
    agency      = models.CharField(max_length=256, default = " ",null=True, blank = True)
    phone       = models.CharField(max_length=40, default = 0,null=True, blank = True)
    address     = models.CharField(max_length=400, null=True, blank = True)
    
    
    def __str__(self):
        return self.user.username

#USER ACTUALLY REFERS TO USERACCOUNT MODEL OR OBJECT JUST USED USER FOR BETTER UNDERSTANDING 
class Token_man():
    
    def __init__(self, user):
        self.user = user
        
    def generate_token(self):
        return secrets.token_urlsafe(40)

    def add_token(self):
        self.user.token = self.generate_token()
        self.user.save()
        print(self.user.token)


class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True,  related_name = 'user')
    token = models.CharField(max_length=60, null=True, blank = True)
    is_active = models.BooleanField(default = True)

    #CHECK IF SESSION TOKEN POSTED IS CORRECT 
    def token_is_correct(self, user_object, client_token, session_token ):
        if user_object.token == client_token and self.token == session_token:
            return True
        else: 
            return False
            
    def disable(self):

        self.is_active = False
        self.save()
    
    def _authenticate(self, auth_data):
        
        if self.token == auth_data['session_token']:
                return True
        return False


    def save(self, *args, **kwargs):
        self.token = secrets.token_hex(20)
        super(Session, self).save(*args, **kwargs)
    
    def __str__(self):              # __unicode__ on Python 2
        return str(self.user)