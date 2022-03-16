import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Category

CATEGORY_LIST = [
    "printing",
    "network",
    "power",
    "security",
    "software",
    "hardware",
    "internet",
    "phone",
]


class Provider(faker.providers.BaseProvider):
    def category_list_provider(self):
        return self.random_element(CATEGORY_LIST)


class Command(BaseCommand):
    help = "Add data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(8):
            fake.add_provider(Provider)
            Category.objects.get_or_create(category=fake.unique.category_list_provider())
