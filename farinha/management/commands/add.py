"""Add an empty snippet."""

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
        if args:
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
