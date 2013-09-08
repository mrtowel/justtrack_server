from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from just_track.api import *

admin.autodiscover()
v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(LocationResource())

urlpatterns = patterns('',
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'', include('social_auth.urls')),
                       url(r'^$', 'just_track.views.home', name='home'),
                       url(r'^api_info/', 'just_track.views.api', name='api'),
                       url(r'^help/', 'just_track.views.help', name='help'),
                       url(r'^api/', include(v1_api.urls)),
)
