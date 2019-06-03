from django.contrib import admin

# Register your models here.
from main.models import Herdsman, Location, Bounds, Farmland, Collection, Incident, Positions
# Register your models here.


class HerdsmanAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name','surname')}
    list_display = ('name','slug', 'address', 'date', )

class LocationAdmin(admin.ModelAdmin):
    ordering = ('-date',)
    list_display = ('herdsman', 'date', 'address', 'speed',)

class FarmlandAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone','community', 'full_name' )

class BoundAdmin(admin.ModelAdmin):
    list_display = ('farmland', 'date',)

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('herdsman', 'start','stop',)

class IncidentAdmin(admin.ModelAdmin):
    list_display = ('user', 'details','date',)

class PositionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'details','date',)


admin.site.register(Herdsman, HerdsmanAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Farmland, FarmlandAdmin)
admin.site.register(Bounds, BoundAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Incident, IncidentAdmin)
admin.site.register(Positions, PositionsAdmin)