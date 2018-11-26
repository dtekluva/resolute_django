from django.contrib import admin
from useraccounts.models import User, UserAccount, Trader, Funds, Transactions, Months, Global_var
# Register your models here.

class UserAccountAdmin(admin.ModelAdmin):
    list_display = (["user", "stays_in", "balance"])

class TraderAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('fname',)}
    list_display = (["fname", "cell_leader", "fund_needed",])

class FundsAdmin(admin.ModelAdmin):
    list_display = (["trader", "amount",])

class TransactionsAdmin(admin.ModelAdmin):
    list_display = ([ "date","user", "month", "amount", "user", "transaction_type",])

class MonthsAdmin(admin.ModelAdmin):
    list_display = ([ "date", "name", "budget"])

class Global_varAdmin(admin.ModelAdmin):
    list_display = ([ "description", "flat", "b_quarters"])


admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(Trader, TraderAdmin)
admin.site.register(Funds, FundsAdmin)
admin.site.register(Transactions, TransactionsAdmin)
admin.site.register(Months, MonthsAdmin)
admin.site.register(Global_var, Global_varAdmin)