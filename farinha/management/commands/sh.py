"""Execute a snippet using the default shell command."""

import os, stat

from tempfile import NamedTemporaryFile

from django.core.management.base import BaseCommand, CommandError

from fabric.api import local

from farinha.models import Snippet


class Command(BaseCommand):

    """Execute a snippet using the default shell command."""

    args = "<snippet_id snippet_id ...>"
    help = "Run the snippet using the default shell."""

    def add_arguments(self, parser):
        """Add optional arguments."""
        parser.add_argument('--args', nargs='?', type=open)

    def handle(self, *args, **options):
        if args:
            with NamedTemporaryFile(delete=False) as f:
                try:
                    s = Snippet.objects.get(pk=int(args[0]))
                    if s.header:
                        f.write(s.header)
                    if s.body:
                        f.write(s.body)
                    if s.footer:
                        f.write(s.footer)

                    f.close()

                    os.chmod(f.name, 0744) 

                    local(f.name)

                except Snippet.DoesNotExist:
                    raise CommandError( "Snippet %s doesn't exist." % s)
