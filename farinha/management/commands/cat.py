"""Export the snippet to a file."""

from django.core.management.base import BaseCommand, CommandError

from tempfile import NamedTemporaryFile

from farinha.models import Snippet


class Command(BaseCommand):

    """Export the snippet to a file."""

    args = "<snippet_id snippet_id ...>"
    help = "Shows snippet's contents with the given ids."

    def handle(self, *args, **options):
        """Receive snippe id list and export to files."""
        if args:
            for snippet_id in args:
                with NamedTemporaryFile(delete=False) as f:
                    try:
                        s = Snippet.objects.get(pk=int(snippet_id))
                        if s.header:
                            f.write(s.header)
                        if s.body:
                            f.write(s.body)
                        if s.footer:
                            f.write(s.footer)
                        self.stdout.write(f.name)
                    except Snippet.DoesNotExist:
                        raise CommandError(
                                "Snippet %s doesn't exist." %
                                snippet_id)
