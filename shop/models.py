from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_length=10, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()