"""
video feed module model
"""

from django.db import models

# Create your models here.
class Video(models.Model):
    """
    Video feed model used for the incoming video feed images
    """
    received_at = models.DateTimeField(auto_now_add=True)
    video_image = models.ImageField(upload_to='videos/')

    def __str__(self):
        return self.received_at
