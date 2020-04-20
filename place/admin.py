from django.contrib import admin
from place.models import Place


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'city', 'state', 'updated_at', 'created_at')
    list_filter = ('name',)


admin.site.register(Place, PlaceAdmin)
