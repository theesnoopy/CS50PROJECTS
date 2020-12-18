from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class listings(models.Model)
    item_title = models.CharField(max_length=64)
    item_description = models.CharField(max_length=256)
    item_price = models.IntegerField()


class bids(models.Model)

