# Generated by Django 5.0.6 on 2024-08-17 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_comment_clients'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='services',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.serves'),
        ),
    ]
