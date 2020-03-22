from django.db import models


# Create your models here.

class UrlModel(models.Model):
    url = models.URLField()
