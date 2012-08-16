from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    '',
    url(r'^authorize$', 'google_credentials.views.authorize'),
    url(r'^callback$', 'google_credentials.views.callback'),
    url(r'^purge$', 'google_credentials.views.purge'),
)
