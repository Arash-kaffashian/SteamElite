# Generated by Django 5.1.1 on 2025-03-03 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_account_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='order',
            name='account',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='products',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='user',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]
