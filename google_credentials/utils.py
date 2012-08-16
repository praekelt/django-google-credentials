from apiclient.discovery import build
from django.conf import settings
import httplib2
from oauth2client.django_orm import Storage
from google_credentials.models import Credentials


def get_service():
    # Load previously stored credentials.
    storage = Storage(Credentials, 'client_id', settings.GA_CLIENT_ID, 'credentials')
    credentials = storage.get()

    # Authorize credentials and return service.
    http = credentials.authorize(httplib2.Http())
    service = build('analytics', 'v3', http=http)
    return service
