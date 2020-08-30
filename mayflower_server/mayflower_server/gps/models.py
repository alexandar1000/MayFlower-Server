from django.db import models

# Create your models here.
class GPS(models.Model):
    received_at = models.DateTimeField(auto_now_add=True)
    header_secs = models.PositiveIntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()

    def __str__(self):
        return '%.8f, %.8f, %.8f' % (self.latitude, self.longitude, self.altitude)