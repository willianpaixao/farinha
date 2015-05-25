"""Add an empty Snippet."""

from django.core.management.base import BaseCommand, CommandError

from farinha.models import Snippet


class Command(BaseCommand):

    """Creates an empty Snippet with the given title.

    Args:
        args (str): List of Snippets to be created.
    """

    args = "<snippet_id snippet_id ...>"
    help = "Creates a empty Snippets with the given titles."

    def handle(self, *args, **options):
        """Iterate throw the list to create the Snippets."""
        if args:
            for t in args:
                s = Snippet(title=t)
                s.save()
        else:
            self.stdout.write("You need to provide at least the Snippet's \
                title.")
