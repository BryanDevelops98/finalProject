# Generated by Django 3.2.9 on 2021-11-29 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxiApp', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='organization',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
