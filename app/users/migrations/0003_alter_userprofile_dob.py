# Generated by Django 4.0.3 on 2022-03-14 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_agency_userprofile_agency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='DOB'),
        ),
    ]