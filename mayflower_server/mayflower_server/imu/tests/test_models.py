from django.test import TestCase
from ..models import IMU


class IMUTest(TestCase):
    """ Test module for IMU model """

    def setUp(self):
        IMU.objects.create(
            header_secs=1, orient_x=0, orient_y=0, orient_z=0, orient_w=0, angular_velocity_roll=10.789,
            angular_velocity_yaw=60.9797, angular_velocity_pitch=15.123, linear_acceleration_forward=25,
            linear_acceleration_up=5, linear_acceleration_left=2.34)
        IMU.objects.create(
            header_secs=2, orient_x=0.0, orient_y=0.0, orient_z=1.0, orient_w=0.7890, angular_velocity_roll=10.789,
            angular_velocity_yaw=60.9797, angular_velocity_pitch=15.123, linear_acceleration_forward=25,
            linear_acceleration_up=5, linear_acceleration_left=2.34)

    def test_toString(self):
        distance_1 = IMU.objects.get(header_secs=1)
        distance_2 = IMU.objects.get(header_secs=2)
        self.assertEqual(
            str(distance_1), "Orientation: (0.000000, 0.000000, 0.000000, 0.000000)\n Angular velocity: (10.789000, 60.979700, 15.123000)\n Linear Acceleration: (25.000000, 5.000000, 2.340000)")
        self.assertEqual(
            str(distance_2), "Orientation: (0.000000, 0.000000, 1.000000, 0.789000)\n Angular velocity: (10.789000, 60.979700, 15.123000)\n Linear Acceleration: (25.000000, 5.000000, 2.340000)")
