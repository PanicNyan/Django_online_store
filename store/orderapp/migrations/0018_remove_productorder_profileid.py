# Generated by Django 4.2.4 on 2023-08-16 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0017_alter_delivery_maxcost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productorder',
            name='profileId',
        ),
    ]
