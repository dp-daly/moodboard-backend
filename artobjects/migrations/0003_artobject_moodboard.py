# Generated by Django 5.0.6 on 2024-07-08 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artobjects', '0002_artobject_img'),
        ('moodboards', '0002_remove_moodboard_artobjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='artobject',
            name='moodboard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='moodboards.moodboard'),
        ),
    ]
