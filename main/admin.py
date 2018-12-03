from django.contrib import admin

# Register your models here.
from main.models import Herdsman, Location, Bound, Farmland, Collection
# Register your models here.


class HerdsmanAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name','surname')}
    list_display = ('name','slug', 'address', 'date', )

class LocationAdmin(admin.ModelAdmin):
    ordering = ('-date',)
    list_display = ('herdsman', 'date', 'address', 'speed',)

class FarmlandAdmin(admin.ModelAdmin):
    list_display = ('owner_name', 'phone','address', )

class BoundAdmin(admin.ModelAdmin):
    list_display = ('farmland', 'date',)

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('herdsman', 'start','stop',)


admin.site.register(Herdsman, HerdsmanAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Farmland, FarmlandAdmin)
admin.site.register(Bound, BoundAdmin)
admin.site.register(Collection, CollectionAdmin)