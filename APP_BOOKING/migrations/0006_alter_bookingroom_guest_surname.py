# Generated by Django 5.0.2 on 2024-03-07 13:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_BOOKING', '0005_alter_bookingroom_guest_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingroom',
            name='guest_surname',
            field=models.ForeignKey(default='Secret', on_delete=django.db.models.deletion.SET_DEFAULT, to='APP_BOOKING.guest'),
        ),
    ]