# Generated by Django 4.2.4 on 2023-08-22 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0024_product_archived'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='salePrice',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='salesCount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='product', to='productapp.tag'),
        ),
    ]
