from django.db import models
from django.urls import reverse

# Create your models here.

class Creatures(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    cstatus = models.CharField(max_length=50) #Conservation Status
    family = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    found = models.CharField(max_length=200)
    size = models.CharField(max_length=100)
    diet = models.CharField(max_length=200)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show', kwargs={'creatures_id': self.id})
