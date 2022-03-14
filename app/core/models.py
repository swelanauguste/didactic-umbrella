import uuid

from django.db import models

from django.conf import settings

User = settings.AUTH_USER_MODEL


class Agency(models.Model):
    agency_name = models.CharField(max_length=100)

    def __str__(self):
        return self.agency_name


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
    # customer = model.For
