# Generated by Django 3.2.20 on 2023-07-23 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0020_alter_booking_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
    ]
