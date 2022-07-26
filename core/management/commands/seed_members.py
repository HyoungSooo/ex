from django_seed import Seed
from core.models import AboutUs

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = 'This command creates users'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number', default=1, type=int, help="How many users do you want to create?"
        )

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        seeder.add_entity(AboutUs, number, {
            'name': lambda x: seeder.faker.name(),
            'category': 'AL',
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} posts created!'))
