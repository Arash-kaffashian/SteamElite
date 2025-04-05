from django.db import models
from django.contrib.auth.models import User

from products.models import Product

from rest_framework.authtoken.models import Token


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    steam_id = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.user.username




