from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    time = models.DateField(auto_now_add=True)
    # image = models.ImageField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name