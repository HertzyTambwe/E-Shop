from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)


    def __str__(self):
        return f"{self.name} ({self.stock})"
    
    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})
    