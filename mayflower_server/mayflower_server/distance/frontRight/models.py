"""
Front Right Distance module model
"""

from django.db import models

# Create your models here.
class FrontRightDistance(models.Model):
    """
    FrontRightDistance model used for the incoming front left distance data
    """
    received_at = models.DateTimeField(auto_now_add=True)
    header_secs = models.PositiveIntegerField()
    distance = models.FloatField()

    def __str__(self):
        return str(self.distance)
