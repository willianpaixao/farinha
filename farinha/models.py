"""Django's modelling files.

Contains all objects and their attributes.
"""

from django.contrib.auth.models import User
from django.db import models


class Snippet(models.Model):

    """Snippet's entiry description."""

    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=512)
    alias = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    header = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    footer = models.TextField(blank=True, null=True)

    def __unicode__(self):
        """Return snippet's title."""
        return self.title

    def get_absolute_url(self):
        """Return model's default route."""
        return reverse('snippet_update', kwargs={'pk': self.pk})
