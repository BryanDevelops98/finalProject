# Generated by Django 3.2.9 on 2021-12-08 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxiApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, 'created'), (2, 'accepted'), (3, 'cancelled')], default=1),
        ),
    ]
