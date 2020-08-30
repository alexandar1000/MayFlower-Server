'''
battery module model
'''

from django.db import models


# Create your models here.
class Battery(models.Model):
    '''
    Battery model is used for the incomming battery data readings
    '''
    received_at = models.DateTimeField(auto_now_add=True)
    header_secs = models.PositiveIntegerField()
    percentage = models.FloatField()
    power_supply_status = models.CharField(max_length=15)

    def __str__(self):
        return str(self.percentage)