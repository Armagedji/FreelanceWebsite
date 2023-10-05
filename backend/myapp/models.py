from django.db import models

# Create your models here.
class freelanceOrder(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    price = models.IntegerField()
    completed = models.BooleanField(default=False)