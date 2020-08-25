'''
battery module model
'''

from django.db import models

# Create your models here.
class BatteryPower(models.Model):
    '''
    Battery model is used for the incomming battery power readings
    '''
    received_at = models.DateTimeField(auto_now_add=True)
    batteryPower = models.FloatField()

    def __str__(self):
        return str(self.batteryPower)