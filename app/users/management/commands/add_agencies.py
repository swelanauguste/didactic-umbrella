import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Agency

AGENCY_LIST = [
    "office of the prime minister",
    "department of the publis service",
    "audit",
    "contact center",
    "planning",
    "land registry",
    "parastatal",
    "housing",
    "NEMO",
    "inland revenue",
    "commerce",
    "GG"
]


class Provider(faker.providers.BaseProvider):
    def agency_list_provider(self):
        return self.random_element(AGENCY_LIST)


class Command(BaseCommand):
    help = "Add data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            fake.add_provider(Provider)
            Agency.objects.get_or_create(agency_name=fake.unique.agency_list_provider())
