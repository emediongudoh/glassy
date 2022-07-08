from django.db import models
from django.conf import settings


class Product(models.Model):
    name = models.CharField(max_length=255) 
    image = models.ImageField(upload_to='products/')    
    price = models.FloatField()

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name
