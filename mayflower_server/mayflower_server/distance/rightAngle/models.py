"""
Right Angle Distance module model
"""

from django.db import models

# Create your models here.
class RightAngleDistance(models.Model):
    """
    RightAngleDistance model used for the incoming right angle distance data
    """
    received_at = models.DateTimeField(auto_now_add=True)
    header_secs = models.PositiveIntegerField()
    distance = models.FloatField()

    def __str__(self):
        return str(self.distance)
