"""Print a given snippet on the standard output."""

from django.core.management.base import BaseCommand, CommandError

from farinha.models import Snippet


class Command(BaseCommand):

    """Print a given snippet on the standard output."""

    args = "<snippet_id snippet_id ...>"
    help = "Shows snippet's contents with the given ids."

    def handle(self, *args, **options):
        """Receive the snippet's titles and store them in the database."""
        if args:
            for s in args:
                try:
                    s = Snippet.objects.get(pk=int(s))
                    if s.header is not None:
                        self.stdout.write(s.header)
                    if s.body is not None:
                        self.stdout.write(s.body)
                    if s.footer is not None:
                        self.stdout.write(s.footer)
                except Snippet.DoesNotExist:
                    raise CommandError("Snippet %s doesn't exist." % s)
