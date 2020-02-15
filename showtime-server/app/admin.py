from django.contrib import admin
from .models import Venue, Artist, Show

admin.site.register(Artist)

class ShowInstanceInline(admin.TabularInline):
    model = Show



@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    inlines = [ShowInstanceInline]

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('name', 'venue', 'kick_off')
    list_filter = ('venue', 'kick_off')

