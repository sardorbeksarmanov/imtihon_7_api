# Generated by Django 5.0.6 on 2024-08-17 13:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_serves_api_serves_status_159a54_idx_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='clients',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.clients'),
        ),
    ]
