from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),
    
    url(r'^google-credentials/', include('google_credentials.urls')),
    
    #(r'^$', 'google_credentials.views.index'),
    #(r'^oauth2callback', 'google_credentials.views.auth_return'),


    url(r'^admin/', include(admin.site.urls)),
)
