# Generated by Django 5.0.6 on 2024-08-18 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_clients_defination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='image',
            field=models.URLField(null=True),
        ),
    ]
