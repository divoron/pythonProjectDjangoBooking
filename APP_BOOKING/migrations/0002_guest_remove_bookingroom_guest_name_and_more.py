# Generated by Django 5.0.2 on 2024-03-02 15:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_BOOKING', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('birth_date', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='bookingroom',
            name='guest_name',
        ),
        migrations.AddField(
            model_name='bookingroom',
            name='guest_surname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='APP_BOOKING.guest'),
        ),
    ]
