# Generated by Django 4.2.4 on 2023-08-16 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0011_productorder_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorder',
            name='count',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
