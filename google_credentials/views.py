from django.conf import settings
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from google_credentials.models import Credentials
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.django_orm import Storage


@staff_member_required
def authorize(request):
    # Fetch client info from settings.
    client_id = settings.GA_CLIENT_ID
    client_secret = settings.GA_CLIENT_SECRET
    redirect_uri = settings.GA_REDIRECT_URI
    scope = settings.GA_SCOPE

    # Load previously stored credentials if available.
    storage = Storage(Credentials, 'client_id', client_id, 'credentials')
    credentials = storage.get()

    # If credentials could not be found authorize.
    if credentials is None or credentials.invalid is True:
        FLOW = OAuth2WebServerFlow(
            client_id=client_id,
            client_secret=client_secret,
            scope=scope,
            redirect_uri=redirect_uri,
        )
        authorize_url = FLOW.step1_get_authorize_url()
        return HttpResponseRedirect(authorize_url)
    # Otherwise return to admin home with success message.
    else:
        messages.info(request, 'Previously authorized %s.' % client_id)
        return HttpResponseRedirect(reverse('admin:index'))


@staff_member_required
def purge(request):
    client_id = settings.GA_CLIENT_ID
    try:
        Credentials.objects.get(client_id=client_id).delete()
        messages.info(request, 'Purged %s.' % client_id)
    except Credentials.DoesNotExist:
        messages.info(request, 'Nor credentials found for %s, nothing purged.' % client_id)

    return HttpResponseRedirect(reverse('admin:index'))


@staff_member_required
def callback(request):
    # Fetch client info from settings.
    client_id = settings.GA_CLIENT_ID
    client_secret = settings.GA_CLIENT_SECRET
    redirect_uri = settings.GA_REDIRECT_URI
    scope = settings.GA_SCOPE

    # Initiate Flow
    FLOW = OAuth2WebServerFlow(
        client_id=client_id,
        client_secret=client_secret,
        scope=scope,
        redirect_uri=redirect_uri,
    )
    credentials = FLOW.step2_exchange(request.REQUEST)

    # Store credentials.
    credentials_obj, created = Credentials.objects.get_or_create(
        client_id=credentials.client_id
    )
    credentials_obj.credentials = credentials
    credentials_obj.save()

    # Return to admin home with success message.
    messages.info(request, 'Authorized %s.' % client_id)
    return HttpResponseRedirect(reverse('admin:index'))
