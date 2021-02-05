from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Incidence, WorldBorder, GPXPoint, GPXTrack, gpxFile

class IncidenceAdmin(LeafletGeoAdmin):
    list_display = ('__str__', 'location')


admin.site.register(Incidence, IncidenceAdmin)
admin.site.register(WorldBorder, LeafletGeoAdmin)

admin.site.register(GPXPoint, LeafletGeoAdmin)
admin.site.register(GPXTrack, LeafletGeoAdmin)
admin.site.register(gpxFile)
