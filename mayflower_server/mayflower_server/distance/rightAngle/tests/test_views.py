import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import RightAngleDistance
from ..serializers import RightAngleDistanceSerializer

# Initialise the APIClient App
client = Client()

class GetAllRightAngleTest(TestCase):
    """ Test module for GET all RightAngleDistances API """

    def setUp(self):
        RightAngleDistance.objects.create(
            header_secs=1, distance="4.1234")
        RightAngleDistance.objects.create(
            header_secs=2, distance="4.1234")
        RightAngleDistance.objects.create(
            header_secs=3, distance="4.1234")
        RightAngleDistance.objects.create(
            header_secs=4, distance="4.1234")

    def test_get_all_rightangle(self):
        # get API response
        response = client.get(reverse('rightangle_list'))
        # get data from db
        rightangle = RightAngleDistance.objects.all()
        serializer = RightAngleDistanceSerializer(rightangle, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleRightAngleDistanceTest(TestCase):
    """ Test module for GET a specific RightAngleDistance API """

    def setUp(self):
        self._1 = RightAngleDistance.objects.create(
            header_secs=1, distance="1.1234")
        self._2 = RightAngleDistance.objects.create(
            header_secs=2, distance="2.1234")
        self._3 = RightAngleDistance.objects.create(
            header_secs=3, distance="3.1234")
        self._4 = RightAngleDistance.objects.create(
            header_secs=4, distance="4.1234")

    def test_get_valid_single_rightangle(self):
        response = client.get(
            reverse('rightangle_detail', kwargs={'pk': self._3.pk})
        )
        rightangle = RightAngleDistance.objects.get(pk=self._3.pk)
        serializer = RightAngleDistanceSerializer(rightangle)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_rightangle(self):
        response = client.get(
            reverse('rightangle_detail', kwargs={'pk': 1000})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewRightAngleDistanceTest(TestCase):
    """ Test module for inserting a new rightangle """

    def setUp(self):
        self.valid_payload = {
            'header_secs': 1,
            'distance': 3.97
        }
        self.invalid_payload = {
            'header_secs': None,
            'distance': 1.234
        }

    def test_create_valid_rightangle(self):
        response = client.post(
            reverse('rightangle_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_rightangle(self):
        response = client.post(
            reverse('rightangle_list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleRightAngleDistanceTest(TestCase):
    """ Test module for deleting an existing rightangle record """

    def setUp(self):
        self._1 = RightAngleDistance.objects.create(
            header_secs=1, distance="1.1234")
        self._2 = RightAngleDistance.objects.create(
            header_secs=2, distance="2.1234")

    def test_valid_delete_rightangle(self):
        response = client.delete(
            reverse('rightangle_detail', kwargs={'pk': self._1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_rightangle(self):
        response = client.delete(
            reverse('rightangle_detail', kwargs={'pk': 1000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)