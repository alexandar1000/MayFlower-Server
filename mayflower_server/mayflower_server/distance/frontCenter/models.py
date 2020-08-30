"""
Front Center Distance module model
"""

from django.db import models


# Create your models here.
class FrontCenterDistance(models.Model):
    """
    FrontCenterDistance model used for the incoming front center distance data
    """
    received_at = models.DateTimeField(auto_now_add=True)
    header_secs = models.PositiveIntegerField()
    distance = models.CharField(max_length=15)

    def __str__(self):
        return str(self.distance)
