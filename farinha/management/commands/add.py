"""Add an empty Snippet."""

from django.core.management.base import BaseCommand, CommandError

from farinha.models import Snippet


class Command(BaseCommand):

    """Creates an empty Snippet with the given title.

    Args:
        args (str): List of Snippets to be created.
    """

    def handle(self, *args, **options):
        """Iterate throw the list to create the Snippets."""
        if args:
            for t in args:
                s = Snippet(title=t)
                s.save()
