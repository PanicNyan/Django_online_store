# Generated by Django 4.2.4 on 2023-08-11 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0009_specification'),
    ]

    operations = [
        migrations.AddField(
            model_name='specification',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='specifications', to='productapp.product'),
            preserve_default=False,
        ),
    ]
