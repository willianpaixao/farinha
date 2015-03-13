from django.core.management.base import BaseCommand, CommandError

from farinha.models import Snippet

class Command(BaseCommand):
    args = "<snippet_id snippet_id ...>"
    help = "List snippets with the given ids."

    def handle(self, *args, **options):
        if args:
            for snippet_id in args:
                try:
                    s = Snippet.objects.get(pk=int(snippet_id))
                    self.stdout.write("%2d\t%s\t\t%s" % (s.pk, s.title, s.alias))
                except Snippet.DoesNotExist:
                    raise CommandError("Snippet %s doesn't exist." % snippet_id)
        else:
            try:
                snippets = Snippet.objects.all()
                if snippets:
                    for s in snippets:
                        self.stdout.write("%2d\t%s\t\t%s" % (s.pk, s.title, s.alias))
                else:
                    self.stdout.write("You have no stored snippets.")
            except Snippet.DoesNotExist:
                raise CommandError("Whoops! I don't know what happened.")

