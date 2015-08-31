"""Add an empty snippet."""

import os

from django.core.management.base import BaseCommand, CommandError

from farinha.models import Snippet


class Command(BaseCommand):

    """Creates an empty snippet with the given title.

    Args:
        args (str): Snippet to be created.
    """

    args = "<snippet_id>"
    help = "Creates a empty snippet with the given title."

    def add_arguments(self, parser):
        """Add optional arguments."""
        parser.add_argument('--header', nargs='?', type=open)
        parser.add_argument('--body', nargs='?', type=open)
        parser.add_argument('--footer', nargs='?', type=open)

    def handle(self, *args, **options):
        """Iterate throw the list to create the snippets."""
        if len(args) == 1:
            if os.path.isfile(args[0]):
                with open(args[0], 'r') as f:
                    s = Snippet(title=args[0])
                    s.body = f.read()
                    s.save()
            else:
                s = Snippet(title=args[0])
                if options['header']:
                    s.header = options['header'].read()
                if options['body']:
                    s.body = options['body'].read()
                if options['footer']:
                    s.footer = options['footer'].read()
                s.save()
        elif args > 1:
            s = Snippet(title=args[0])
            if options['header']:
                s.header = options['header'].read()
#            else:
#                with open('farinha/header.txt', 'r') as f:
#                    s.header = f.read()
            if options['body']:
                s.body = options['body'].read()
#            else:
#                with open('farinha/body.txt', 'r') as f:
#                    s.body = f.read()
            if options['footer']:
                s.footer = options['footer'].read()
#            else:
#                with open('farinha/footer.txt', 'r') as f:
#                    s.footer = f.read()
            s.save()
        else:
            self.stdout.write("You need to provide at least the snippet's \
                title.")
