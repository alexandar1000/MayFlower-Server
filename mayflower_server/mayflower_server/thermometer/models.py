'''
thermometer module model
'''
from django.db import models

# Create your models here.
class Temperature(models.Model):
    '''
    Temperature model used for the incoming temperature readings
    '''
    temperature = models.FloatField()

    def __str__(self):
        return self.temperature
