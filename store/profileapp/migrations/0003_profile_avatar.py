# Generated by Django 4.2.4 on 2023-08-06 08:21

from django.db import migrations, models
import profileapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0002_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=profileapp.models.profile_avatar_directory_path),
        ),
    ]
