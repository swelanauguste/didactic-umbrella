# Generated by Django 4.0.3 on 2022-03-15 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_ticket_customer_ticket_created_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_categories', to='core.ticketstatus'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_detail',
            field=models.TextField(blank=True, null=True),
        ),
    ]
