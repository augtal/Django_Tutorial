from django.contrib import admin

from .models import Meetup, Location, Participant

# Register your models here.

class MeetUpAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('location',)
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Meetup, MeetUpAdmin)
admin.site.register(Location)
admin.site.register(Participant)