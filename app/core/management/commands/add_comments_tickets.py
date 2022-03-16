import random

from django.core.management.base import BaseCommand
from faker import Faker
from users.models import User

from ...models import Ticket, TicketComment


class Command(BaseCommand):
    help = "Add data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(6):
            TicketComment.objects.get_or_create(
                ticket=Ticket.objects.get(pk=random.randint(1, 6)),
                comment=fake.text(max_nb_chars=200),
                created_by=User.objects.get(pk=random.randint(1, 6)),
                updated_by=User.objects.get(pk=random.randint(1, 6)),
            )
