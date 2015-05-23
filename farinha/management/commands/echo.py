from django.core.management.base import BaseCommand, CommandError

from farinha.models import Snippet


class Command(BaseCommand):
    args = "<snippet_id snippet_id ...>"
    help = "Shows snippet's contents with the given ids."

    def handle(self, *args, **options):
        if args:
            for snippet_id in args:
                try:
                    s = Snippet.objects.get(pk=int(snippet_id))
                    if s.header is not None:
                        self.stdout.write(s.header)
                    if s.body is not None:
                        self.stdout.write(s.body)
                    if s.footer is not None:
                        self.stdout.write(s.footer)
                except Snippet.DoesNotExist:
                    raise CommandError("Snippet %s doesn't exist." % snippet_id)
