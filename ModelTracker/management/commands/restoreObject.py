from django.core.management.base import BaseCommand
from ModelTracker.models import History


class Command(BaseCommand):
    help = 'Restore Object to old status'

    def add_arguments(self, parser):
        parser.add_argument('--id', nargs='?', type=str,default=None)
        # parser.add_argument("--state",type=str,nargs='?',default="new")
        parser.add_argument("--user",type=str,nargs='?',default="CLI")


    def handle(self, *args, **options):
        if not options.get("id",None):
            print ("Change ID is needed")
            exit(1)

        h = History.objects.get(id=int(options["id"]))
        m = h.get_object()
        m.save(options["user"],event_name="Restore Record to %s (%s)"%(options["id"],options["state"]))




