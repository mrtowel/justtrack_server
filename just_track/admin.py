from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import *


class JustTrackUserProfileInline(admin.StackedInline):
    model = JustTrackUser


class LocationUserInline(admin.StackedInline):
    model = Location
    extra = 1


class JustTrackUserAdmin(UserAdmin):
    inlines = [JustTrackUserProfileInline, LocationUserInline, ]


class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ('time', 'user', 'lon', 'lat', )
    ordering = ('-time', 'user', )


admin.site.unregister(User)
admin.site.register(User, JustTrackUserAdmin)
admin.site.register(Location, LocationAdmin)
