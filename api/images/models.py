from django.db import models


# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=255)
    size_in_bytes = models.BigIntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
