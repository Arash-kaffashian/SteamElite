# Generated by Django 5.1.1 on 2025-02-17 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_account_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
    ]
