from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import date, datetime

# Create your models here.
class Herdsman(models.Model):
    name            = models.CharField(max_length=40,unique=False)
    surname         = models.CharField(max_length=40,unique=False)
    phone           = models.IntegerField(unique=False, default = "00000000")
    userid          = models.IntegerField(default=0)
    lng             = models.FloatField(max_length=100,blank=True, default=0)
    lat             = models.FloatField(max_length=100,blank=True, default=0)
    slug            = models.SlugField(blank=True,unique=True)
    address         = models.TextField(default=0)
    state         = models.TextField(default=0)
    last_post       = models.DateField(auto_now_add=True, blank=True)
    is_trespassing  = models.BooleanField(default = False)
    date            = models.DateField(auto_now_add=True)
    db_id           = models.CharField(max_length=40, unique=True, null = True, blank=True)
    no_of_cattle    = models.IntegerField(unique=False, default = "0")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Herdsman, self).save(*args, **kwargs)
        self.db_id = 'hd{:03d}'.format(self.id)
        super(Herdsman, self).save(*args, **kwargs)

    def __str__(self):              # __unicode__ on Python 2
        return self.slug

    class Meta:
        ordering = ('slug',)


class Collection(models.Model):
    herdsman = models.ForeignKey('Herdsman', on_delete=models.CASCADE)
    start = models.DateTimeField(default=datetime.now(), blank=True)
    stop = models.DateTimeField(default=datetime.now(), blank=True)


class Location(models.Model):
    herdsman        = models.ForeignKey('Herdsman', on_delete=models.CASCADE)
    collection      = models.ForeignKey('Collection', on_delete=models.CASCADE, default = 1)
    lng             = models.FloatField(max_length=100,blank=True, default=0)
    lat             = models.FloatField(max_length=100,blank=True, default=0)
    speed           = models.FloatField(max_length=100,blank=True, default=0)
    accuracy        = models.FloatField(max_length=100,blank=True, default=0)
    address         = models.TextField(default=0)
    state           = models.TextField(default=0)
    date            = models.DateTimeField(default=datetime.now(), blank=True)
    

    def __str__(self):              # __unicode__ on Python 2
        return str(self.lat) + str(self.lng)

    class Meta:
        ordering = ('date',)


class Farmland(models.Model):
    user       = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'farmland', null = True, blank = True, default = 1)
    community  = models.TextField(default=0)
    full_name  = models.CharField(max_length=50, null = True)
    phone      = models.CharField(max_length=20, unique=True)
    token       = models.CharField(max_length=60, null=True, blank = True)
    db_id           = models.CharField(max_length=40,unique=True, null = True, blank=True )

    def __str__(self):              # __unicode__ on Python 2
        return str(self.user.username)
    
    def save(self, *args, **kwargs):
        
        super(Farmland, self).save(*args, **kwargs)
        self.db_id = 'hd{:03d}'.format(self.id)
        super(Farmland, self).save(*args, **kwargs)


class Bounds(models.Model):
    farmland        = models.ForeignKey('Farmland', on_delete=models.CASCADE)
    lng             = models.FloatField(max_length=100,blank=True, default=0)
    lat             = models.FloatField(max_length=100,blank=True, default=0)
    speed           = models.FloatField(max_length=100,blank=True, default=0)
    accuracy        = models.FloatField(max_length=100,blank=True, default=0)
    address         = models.TextField(default=0)
    date            = models.DateTimeField(auto_now_add=True)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.lat) + str(self.lng)

    class Meta:
        ordering = ('date',)