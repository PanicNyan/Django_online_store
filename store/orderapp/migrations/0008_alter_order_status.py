# Generated by Django 4.2.4 on 2023-08-16 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0007_alter_order_paymenttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='accepted', max_length=30),
        ),
    ]
