from django.db import models

# Create your models here.
class Temperature(models.Model):
    temperature = models.FloatField()

    def __str__(self):
        return self.temperature