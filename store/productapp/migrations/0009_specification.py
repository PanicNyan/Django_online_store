# Generated by Django 4.2.4 on 2023-08-11 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0008_review_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=20)),
            ],
        ),
    ]
