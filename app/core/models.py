from email.policy import default
import uuid

from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

User = settings.AUTH_USER_MODEL


class TicketStatus(models.Model):
    ticket_status = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "tickets statuses"

    def __str__(self):
        return self.ticket_status.upper()


class Category(models.Model):
    category = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category


class Ticket(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    slug = models.SlugField(max_length=65, blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="ticket_categories",
        null=True,
        blank=True,
    )
    ticket_status = models.ForeignKey(
        TicketStatus, on_delete=models.CASCADE, related_name="ticket_statuses", default=5
    )
    ticket_title = models.CharField(max_length=100)
    ticket_detail = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ticket_created_by", null=True
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ticket_updated_by", null=True
    )
    
    def get_absolute_url(self):
        return reverse('core:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.uid)
        super(Ticket, self).save(*args, **kwargs)

    def __str__(self):
        return self.ticket_title


class TicketComment(models.Model):
    ticket = models.ForeignKey(
        Ticket, on_delete=models.CASCADE, related_name="comments", null=True, blank=True
    )
    comment = models.TextField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_created_by"
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_updated_by"
    )

    def __str__(self):
        return self.comment + " | " + self.ticket.ticket_title
