# Generated by Django 5.0.6 on 2024-08-17 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_advise_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='username',
            field=models.CharField(default='default_username', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='serves',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
