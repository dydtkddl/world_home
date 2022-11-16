from django.db import models

# Create your models here.
class continent_factor(models.Model):
    대륙 = models.CharField(max_length=1000)
    factor = models.CharField(max_length=1000)
    death_per_100000 = models.CharField(max_length=1000)

