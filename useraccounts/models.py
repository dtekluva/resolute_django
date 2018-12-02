import time
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import date
from django.db import models
# Create your models here.

class UserAccount(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'useraccount')
    agency      = models.CharField(max_length=256, default = " ",null=True, blank = True)
    phone       = models.CharField(max_length=40, default = 0,null=True, blank = True)
    address     = models.CharField(max_length=40, null=True, blank = True)
    
    def __str__(self):
        return self.user.username