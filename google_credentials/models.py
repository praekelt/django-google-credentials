from django.db import models
from oauth2client.django_orm import CredentialsField


class Credentials(models.Model):
    client_id = models.CharField(
        max_length=128
    )
    credentials = CredentialsField(
        editable=False
    )
