from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=25, default='')
    units = models.PositiveIntegerField(default=0)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to="fruits")