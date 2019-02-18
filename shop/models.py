from django.db import models
from django.conf import settings

# Create your models here.
class ShopInfo(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    address = models.CharField(max_length=200)

class Item(models.Model):
    shop = models.ForeignKey(ShopInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    is_public = models.BooleanField(default=False)
