# Generated by Django 4.2.4 on 2023-08-11 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0004_tag_product_alter_product_freedelivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fullDescription',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]