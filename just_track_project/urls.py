from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'just_track_project.views.home', name='home'),
                       # url(r'^just_track_project/', include('just_track_project.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'', include('social_auth.urls')),
                       url(r'^$', 'just_track.views.home', name='home'),
                       url(r'^api/', 'just_track.views.api', name='api'),
                       url(r'^help/', 'just_track.views.help', name='help'),
)
