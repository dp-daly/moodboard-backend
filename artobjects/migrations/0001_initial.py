# Generated by Django 5.0.6 on 2024-07-04 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artobject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, null=True)),
                ('artist', models.CharField(blank=True, max_length=70, null=True)),
                ('api_object', models.CharField(max_length=150)),
                ('user_text', models.TextField(blank=True, max_length=1000, null=True)),
                ('owner', models.CharField()),
            ],
        ),
    ]
