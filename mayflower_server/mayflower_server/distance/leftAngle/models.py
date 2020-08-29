"""
Left Angle Distance module model
"""

from django.db import models

# Create your models here.
class LeftAngleDistance(models.Model):
    """
    LeftAngleDistance model used for the incoming left angle distance data
    """
    received_at = models.DateTimeField(auto_now_add=True)
    header_secs = models.IntegerField()
    distance = models.FloatField()

    def __str__(self):
        return str(self.distance)
