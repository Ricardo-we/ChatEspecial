# Generated by Django 3.2.5 on 2021-09-23 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messages',
            options={'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
        migrations.AlterModelOptions(
            name='rooms',
            options={'verbose_name': 'Room', 'verbose_name_plural': 'Rooms'},
        ),
    ]
