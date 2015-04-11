from django.conf import settings
from django.db import models

from .storage import PublicStorage


class Profile(models.Model):
    """
    Represents profile information for a user of the guide.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    url = models.CharField(max_length=256)


class Tool(models.Model):
    """
    Represents a Quantified Self tool.
    """

    approved = models.BooleanField()
    created = models.DateTimeField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.TextField()
    name = models.CharField(max_length=256)
    url = models.CharField(max_length=512)
    image = models.ImageField(blank=True,
                              max_length=1024,
                              storage=PublicStorage(),
                              upload_to='images/tools')


class Screenshot(models.Model):
    """
    Represents one screenshot of a tool.
    """

    tool = models.ForeignKey(Tool, related_name='screenshots')
    image = models.FilePathField()
    description = models.TextField()
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL)
