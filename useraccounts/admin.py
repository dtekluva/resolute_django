from django.contrib import admin
from useraccounts.models import User, UserAccount
# Register your models here.

class UserAccountAdmin(admin.ModelAdmin):
    list_display = (["user", "phone", "address"])

admin.site.register(UserAccount, UserAccountAdmin)