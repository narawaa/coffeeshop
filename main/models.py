from django.db import models
from django.contrib.auth.models import User
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    time = models.DateField(auto_now_add=True)
    stock = models.IntegerField()

    def __str__(self):
        return self.name