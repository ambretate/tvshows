from django.db import models

# Create your models here.
class TVshow(models.Model):
    name = models.CharField(max_length=None)
    provider = models.CharField(max_length=100)
    review = models.CharField(max_length = None)


    def __str__(self):
        return self.name