"""
lidar module model
"""

from django.contrib.postgres.fields.jsonb import JSONField as JSONBField
from django.db import models

# Create your models here.
class Lidar3D(models.Model):
    """
    3D Lidar model used for the incoming CloudPoints data
    """
    received_at = models.DateTimeField(auto_now_add=True)
    height = models.IntegerField()
    width = models.IntegerField()
    fields = JSONBField(default=list, null=True, blank=True)
    is_bigendian = models.BooleanField()
    point_step = models.IntegerField()
    row_step = models.IntegerField()
    data = models.BinaryField()
    is_dense = models.BooleanField()

    def __str__(self):
        return str(self.received_at)

# class PointField(medels.Model):
#     name = models.CharField(max_length=1)
#     offset = models.IntegerField()
#     dataType = models.BinaryField()
#     count = 1