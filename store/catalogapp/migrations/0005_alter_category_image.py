# Generated by Django 4.2.4 on 2023-08-22 06:25

import catalogapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogapp', '0004_category_archived'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to=catalogapp.models.category_image_upload_path),
        ),
    ]
