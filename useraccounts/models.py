import time
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import date
from django.db import models
# Create your models here.

class UserAccount(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation  = models.CharField(max_length=256, default = " ",null=True, blank = True)
    # cell        = models.CharField(max_length=256, default = " ",null=True, blank = True)
    is_active   = models.BooleanField( blank = True, default = True)
    phone       = models.CharField(max_length=40, default = 0,null=True, blank = True)
    dob         = models.DateField(max_length=40, default = "",null=True, blank = True)
    address     = models.CharField(max_length=40, null=True, blank = True)
    stays_in    = models.CharField(max_length=40, null=True, default = "flat")
    fee         = models.IntegerField(null=True, blank = True)
    has_special_fee   = models.BooleanField( blank = True, default = False)
    balance     = models.IntegerField(null = True, blank = True)
    fname       = models.CharField(max_length=40, null=True, default = "New")
    lname       = models.CharField(max_length=40, null=True, default = "User")
    
    def __str__(self):
        return self.user.username

# class Months(models.Model):
#     name    = models.CharField(max_length=40, default = 0,null=True, blank = True)
#     date    = models.DateField(max_length=40, default = "2018-03-15",null=True, blank = True)
#     budget  = models.IntegerField(null=True, blank = True, default = 0)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = 'Month'

# class Transactions(models.Model):
#     target_month  = models.ForeignKey(Months, on_delete = models.CASCADE, default= "admin")
#     amount  = models.IntegerField(null=True, blank = True)
#     month   = models.CharField(max_length=40, default = 0,null=True, blank = True)
#     user    = models.ForeignKey(User, on_delete = models.CASCADE)
#     date    = models.DateField(max_length=40, default = "2018-03-15",null=True, blank = True)
#     transaction_type = models.CharField(max_length=9, null=True, default = "income")
#     description = models.CharField(max_length=200, null=True, default = "income")

#     class Meta:
#         verbose_name = 'Transaction'

#     def __str__(self):
#         return self.description

# class Global_var(models.Model):
#     flat        = models.IntegerField(default = 26000)
#     b_quarters  = models.IntegerField(default = 12400)
#     description = models.CharField(max_length=40, default = "Global_Variables", blank = True)

#     def __str__(self):
#         return self.description

# class Trader(models.Model):
#     occupation  = models.CharField(max_length=256, null=True, blank = True)
#     phone       = models.CharField(max_length=40, null=True, blank = True)
#     fname       = models.CharField(max_length=40, null=True, blank = True)
#     lname       = models.CharField(max_length=40, null=True, blank = True)
#     dob         = models.DateField(max_length=40, null=True, blank = True)
#     city        = models.CharField(max_length=40, null=True, blank = True)
#     address     = models.CharField(max_length=40, null=True, blank = True)
#     trade_address   = models.CharField(max_length=50, null=True, blank = True)
#     products    = models.CharField(max_length=40, null=True, blank = True)
#     business_date    =  models.DateField(max_length=40, null=True, blank = True)
#     business_worth    = models.IntegerField(null=True, blank = True)
#     have_kids    = models.BooleanField( blank = True)
#     num_kids     = models.IntegerField(null=True, blank = True)
#     with_spouse    = models.BooleanField( blank = True)
#     why_no_spouse    = models.CharField(max_length=20, null=True, blank = True)
#     business_needs    = models.CharField(max_length=40, null=True, blank = True)
#     income     = models.IntegerField(null=True, blank = True)
#     supplier    = models.CharField(max_length=20, null=True, blank = True)
#     change_business    = models.BooleanField( blank = True)
#     fund_needed     = models.IntegerField(null=True, blank = True)
#     do_you_save     = models.BooleanField( blank = True)
#     cell_leader     = models.ForeignKey(User, on_delete = models.CASCADE)
#     cell_name        = models.CharField(max_length=40, null=True, blank = True)
#     added   = models.DateField( auto_now=True)
#     slug        = models.SlugField(max_length=150, unique=True ,db_index=True)

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.fname) + slugify(self.lname) + slugify(self.phone)
#         super(Trader, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.fname + self.lname

# class Funds(models.Model):
#     amount  = models.IntegerField(null=True, blank = True)
#     trader  = models.ForeignKey(Trader, on_delete = models.CASCADE)

#     class Meta:
#         verbose_name = 'Fund'
