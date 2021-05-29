from django.core.management.base import BaseCommand, CommandError
from urlshortener.models import OMMNUrl

class Command(BaseCommand):
    help = 'Refreshes all shortcodes'

    def add_arguments(self, parser):
         parser.add_argument('items', type=int)

    def handle(self, *args, **options):
        return OMMNUrl.objects.refresh_shortcodes(items = options['items'])
