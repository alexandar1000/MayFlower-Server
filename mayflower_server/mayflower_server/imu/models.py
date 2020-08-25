'''

imu module model
'''
from django.db import models

# Create your models here.
class IMU(models.Model):
    '''
    IMU model used for the incoming imuData readings
    '''
    received_at = models.DateTimeField(auto_now_add=True)
    orient_x = models.FloatField()
    orient_y = models.FloatField()
    orient_z = models.FloatField()
    orient_w = models.FloatField()
    angular_velocity_roll = models.FloatField()
    angular_velocity_yaw = models.FloatField()
    angular_velocity_pitch = models.FloatField()
    linear_acceleration_forward = models.FloatField()
    linear_acceleration_up = models.FloatField()
    linear_acceleration_left = models.FloatField()

    def getOrientation(self):
        return '(%f, %f, %f, %f)' % (self.orient_x, self.orient_y, self.orient_z, self.orient_w)

    def getAngularVelocity(self):
        return '%f, %f, %f' % (self.angular_velocity_roll, self.angular_velocity_yaw, self.angular_velocity_pitch)

    def getLinearAcceleration(self):
        return '%f, %f, %f' % (self.linear_acceleration_forward, self.linear_acceleration_up, self.linear_acceleration_left)

    def __str__(self):
        return "Orientation: " + self.getOrientation() + "\n Angular velocity: " + self.getAngularVelocity() + "\n Linear Acceleration: " + self.getLinearAcceleration()