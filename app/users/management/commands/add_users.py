import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Agency, User

TICKET_STATUS_LIST = [
    "awaiting user action",
    "awaiting third party action",
    "awaiting part",
    "awaiting technician's action",
    "awaiting networking action",
    "awaiting systems action",
]


class Provider(faker.providers.BaseProvider):
    def ticket_status_list_provider(self):
        return self.random_element(TICKET_STATUS_LIST)


class Command(BaseCommand):
    help = "Add data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(6):
            fake.add_provider(Provider)
            User.objects.get_or_create(
                username=fake.unique.last_name_male(),
                email=fake.unique.email().lower(),
                password="superuser",
            )
