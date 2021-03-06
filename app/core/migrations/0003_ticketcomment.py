# Generated by Django 4.0.3 on 2022-03-15 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_delete_agency_ticket_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
