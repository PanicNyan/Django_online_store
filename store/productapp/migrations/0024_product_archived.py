# Generated by Django 4.2.4 on 2023-08-22 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0023_alter_product_options_alter_productimage_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
