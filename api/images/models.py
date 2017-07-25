from django.db import models


# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=255, unique=True)
    size_in_bytes = models.BigIntegerField()
    version = models.CharField(max_length=25)
    created = models.DateTimeField()
    updated = models.DateTimeField()
