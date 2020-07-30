from django.db import models

# Create your models here.
class Controls(models.Model):
    command = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.command