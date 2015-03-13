from django.core.management.base import BaseCommand, CommandError

from farinha.models import Snippet

class Command(BaseCommand):
    args = "<snippet_id snippet_id ...>"
    help = "Delete snippets with the given id."

    def handle(self, *args, **options):
        for snippet_id in args:
            try:
                s = Snippet.objects.get(pk=int(snippet_id))
            except Snippet.DoesNotExist:
                raise CommandError("Snippet %s doesn't exist." % snippet_id)
            s.delete()

