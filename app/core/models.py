import uuid

from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class TicketStatus(models.Model):
    ticket_status = models.CharField(max_length=100)

    def __str__(self):
        return self.ticket_status


class Ticket(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    ticket_status = models.ForeignKey(
        TicketStatus, on_delete=models.CASCADE, related_name="ticket_statuses"
    )
    ticket_title = models.CharField(max_length=100)
    ticket_detail = models.TimeField(blank=True, null=True)
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customers", null=True, blank=True
    )

    def __str__(self):
        return self.ticket_title
