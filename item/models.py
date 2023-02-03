from django.db import models
from django.contrib.auth.models import User
from category.models import Category


# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_sold = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
