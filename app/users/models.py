import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

# from django.urls import reverse


class User(AbstractUser):
    is_help_desk = models.BooleanField(default=False)
    is_tech = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)


class UserProfile(models.Model):
    GENDER_LIST = [
        ("M", "M"),
        ("F", "F"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=65, blank=True)
    last_name = models.CharField(max_length=65, blank=True)
    slug = models.SlugField(max_length=65, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_LIST)
    dob = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=25, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.uid)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.user.username
