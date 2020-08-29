"""
Front Left Distance module model
"""

from django.db import models

# Create your models here.
class FrontLeftDistance(models.Model):
    """
    FrontLeftDistance model used for the incoming front left distance data
    """
    received_at = models.DateTimeField(auto_now_add=True)
    header_secs = models.IntegerField()
    distance = models.FloatField()

    def __str__(self):
        return str(self.distance)
