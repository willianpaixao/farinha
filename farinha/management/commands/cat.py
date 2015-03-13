from django.core.management.base import BaseCommand, CommandError

from tempfile import NamedTemporaryFile

from farinha.models import Snippet

class Command(BaseCommand):
    args = "<snippet_id snippet_id ...>"
    help = "Shows snippet's contents with the given ids."

    def handle(self, *args, **options):
        if args:
            for snippet_id in args:
                with NamedTemporaryFile(delete=False) as f:
                    try:
                        s = Snippet.objects.get(pk=int(snippet_id))
                        f.write(s.header)
                        f.write(s.body)
                        f.write(s.footer)
                    except Snippet.DoesNotExist:
                        raise CommandError("Snippet %s doesn't exist." % snippet_id)