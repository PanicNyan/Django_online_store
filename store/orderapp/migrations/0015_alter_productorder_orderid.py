# Generated by Django 4.2.4 on 2023-08-16 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0014_remove_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productorder',
            name='orderId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='orderapp.order'),
        ),
    ]
