# Generated by Django 5.1.1 on 2025-02-07 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='steam_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
