import random

from django.core.management.base import BaseCommand
from faker import Faker
from users.models import User

from ...models import Category, Ticket, TicketStatus


class Command(BaseCommand):
    help = "Add data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(6):
            Ticket.objects.get_or_create(
                category=Category.objects.get(id=random.randint(1, 6)),
                ticket_status=TicketStatus.objects.get(id=random.randint(1, 6)),
                ticket_title=fake.sentence(nb_words=10),
                ticket_detail=fake.text(max_nb_chars=200),
                created_by=User.objects.get(pk=random.randint(1, 6)),
                updated_by=User.objects.get(pk=random.randint(1, 6)),
            )
