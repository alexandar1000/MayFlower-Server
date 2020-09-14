import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import IMU
from ..serializers import IMUSerializer

# Initialise the APIClient App
client = Client()

class GetAllFrontCenterTest(TestCase):
    """ Test module for GET all IMUs API """

    def setUp(self):
        IMU.objects.create(
            header_secs=1, orient_x=0, orient_y=0, orient_z=0, orient_w=0, angular_velocity_roll=10.789,
            angular_velocity_yaw=60.9797, angular_velocity_pitch=15.123, linear_acceleration_forward=25,
            linear_acceleration_up=5, linear_acceleration_left=2.34)
        IMU.objects.create(
            header_secs=2, orient_x=0, orient_y=0, orient_z=0, orient_w=0, angular_velocity_roll=10.789,
            angular_velocity_yaw=60.9797, angular_velocity_pitch=15.123, linear_acceleration_forward=25,
            linear_acceleration_up=5, linear_acceleration_left=2.34)
        IMU.objects.create(
            header_secs=3, orient_x=0, orient_y=0, orient_z=0, orient_w=0, angular_velocity_roll=10.789,
            angular_velocity_yaw=60.9797, angular_velocity_pitch=15.123, linear_acceleration_forward=25,
            linear_acceleration_up=5, linear_acceleration_left=2.34)
        IMU.objects.create(
            header_secs=4, orient_x=0, orient_y=0, orient_z=0, orient_w=0, angular_velocity_roll=10.789,
            angular_velocity_yaw=60.9797, angular_velocity_pitch=15.123, linear_acceleration_forward=25,
            linear_acceleration_up=5, linear_acceleration_left=2.34)

    def test_get_all_imu(self):
        # get API response
        response = client.get(reverse('imu_list'))
        # get data from db
        imu = IMU.objects.all()
        serializer = IMUSerializer(imu, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleIMUTest(TestCase):
    """ Test module for GET a specific IMU API """

    def setUp(self):
        self._1 = IMU.objects.create(
            header_secs=1, orient_x=0, orient_y=0, orient_z=0, orient_w=0, angular_velocity_roll=10.789,
            angular_velocity_yaw=60.9797, angular_velocity_pitch=15.123, linear_acceleration_forward=25,
            linear_acceleration_up=5, linear_acceleration_left=2.34)
        self._2 = IMU.objects.create(
            header_secs=2, orient_x=0, orient_y=0, orient_z=0, orient_w=0, angular_velocity_roll=10.789,
            angular_velocity_yaw=60.9797, angular_velocity_pitch=15.123, linear_acceleration_forward=25,
            linear_acceleration_up=5, linear_acceleration_left=2.34)
        self._3 = IMU.objects.create(
            header_secs=3, orient_x=0, orient_y=0, orient_z=0, orient_w=0, angular_velocity_roll=10.789,
            angular_velocity_yaw=60.9797, angular_velocity_pitch=15.123, linear_acceleration_forward=25,
            linear_acceleration_up=5, linear_acceleration_left=2.34)
        self._4 = IMU.objects.create(
            header_secs=4,  orient_x=0, orient_y=0, orient_z=0, orient_w=0, angular_velocity_roll=10.789,
            angular_velocity_yaw=60.9797, angular_velocity_pitch=15.123, linear_acceleration_forward=25,
            linear_acceleration_up=5, linear_acceleration_left=2.34)

    def test_get_valid_single_imu(self):
        response = client.get(
            reverse('imu_detail', kwargs={'pk': self._3.pk})
        )
        imu = IMU.objects.get(pk=self._3.pk)
        serializer = IMUSerializer(imu)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_imu(self):
        response = client.get(
            reverse('imu_detail', kwargs={'pk': 1000})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewIMUTest(TestCase):
    """ Test module for inserting a new imu """

    def setUp(self):
        self.valid_payload = {
            'header_secs': 1,
            'orient_x': 0,
            'orient_y': 0,
            'orient_z': 0,
            'orient_w': 0,
            'angular_velocity_roll': 10.789,
            'angular_velocity_yaw': 60.9797,
            'angular_velocity_pitch': 15.123,
            'linear_acceleration_forward': 25,
            'linear_acceleration_up': 5,
            'linear_acceleration_left': 2.34
        }
        self.invalid_payload = {
            'header_secs': None,
            'orient_x': 0,
            'orient_y': 0,
            'orient_z': 0,
            'orient_w': 0,
            'angular_velocity_roll': 10.789,
            'angular_velocity_yaw': 60.9797,
            'angular_velocity_pitch': 15.123,
            'linear_acceleration_forward': 25,
            'linear_acceleration_up': 5,
            'linear_acceleration_left': 2.34
        }

    def test_create_valid_imu(self):
        response = client.post(
            reverse('imu_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_imu(self):
        response = client.post(
            reverse('imu_list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleIMUTest(TestCase):
    """ Test module for deleting an existing imu record """

    def setUp(self):
        self._1 = IMU.objects.create(
            header_secs=1, orient_x=0, orient_y=0, orient_z=0, orient_w=0, angular_velocity_roll=10.789,
            angular_velocity_yaw=60.9797, angular_velocity_pitch=15.123, linear_acceleration_forward=25,
            linear_acceleration_up=5, linear_acceleration_left=2.34)
        self._2 = IMU.objects.create(
            header_secs=2, orient_x=0, orient_y=0, orient_z=0, orient_w=0, angular_velocity_roll=10.789,
            angular_velocity_yaw=60.9797, angular_velocity_pitch=15.123, linear_acceleration_forward=25,
            linear_acceleration_up=5, linear_acceleration_left=2.34)

    def test_valid_delete_imu(self):
        response = client.delete(
            reverse('imu_detail', kwargs={'pk': self._1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_imu(self):
        response = client.delete(
            reverse('imu_detail', kwargs={'pk': 1000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)