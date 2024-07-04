# Generated by Django 5.0.6 on 2024-07-04 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artobjects', '0003_alter_artobject_owner'),
        ('moodboards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moodboard',
            name='artobjects',
            field=models.ManyToManyField(blank=True, related_name='moodboards', to='artobjects.artobject'),
        ),
    ]
