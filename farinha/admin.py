"""Django's adminstrator settings."""

from django.contrib import admin

from farinha.models import Snippet

admin.site.register(Snippet)
