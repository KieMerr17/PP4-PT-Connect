# Generated by Django 3.2.19 on 2023-05-26 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0002_rename_request_space_make_booking_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Make_Booking',
            new_name='Booking',
        ),
    ]