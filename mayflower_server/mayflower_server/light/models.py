"""
light module model
"""

from django.db import models

# Create your models here.
class Light(models.Model):
    """
    Light model used for the incoming illuminance data
    """
    received_at = models.DateTimeField(auto_now_add=True)
    illuminate = models.FloatField()
    variance = models.FloatField()

    def __str__(self):
        return str(self.illuminate)
