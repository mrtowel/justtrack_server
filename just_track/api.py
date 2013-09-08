from tastypie.resources import ModelResource
from django.contrib.auth.models import User

from .models import *


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        allowed_methods = ['get']


class LocationResource(ModelResource):
    class Meta:
        queryset = Location.objects.all()
        resource_name = 'locations'
        allowed_methods = ['get', 'post']