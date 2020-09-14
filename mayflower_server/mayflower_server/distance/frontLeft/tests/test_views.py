import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import FrontLeftDistance
from ..serializers import FrontLeftDistanceSerializer

# Initialise the APIClient App
client = Client()

class GetAllFrontLeftTest(TestCase):
    """ Test module for GET all FrontLeftDistances API """

    def setUp(self):
        FrontLeftDistance.objects.create(
            header_secs=1, distance="4.1234")
        FrontLeftDistance.objects.create(
            header_secs=2, distance="4.1234")
        FrontLeftDistance.objects.create(
            header_secs=3, distance="4.1234")
        FrontLeftDistance.objects.create(
            header_secs=4, distance="4.1234")

    def test_get_all_frontleft(self):
        # get API response
        response = client.get(reverse('frontleft_list'))
        # get data from db
        frontleft = FrontLeftDistance.objects.all()
        serializer = FrontLeftDistanceSerializer(frontleft, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleFrontLeftDistanceTest(TestCase):
    """ Test module for GET a specific FrontLeftDistance API """

    def setUp(self):
        self._1 = FrontLeftDistance.objects.create(
            header_secs=1, distance="1.1234")
        self._2 = FrontLeftDistance.objects.create(
            header_secs=2, distance="2.1234")
        self._3 = FrontLeftDistance.objects.create(
            header_secs=3, distance="3.1234")
        self._4 = FrontLeftDistance.objects.create(
            header_secs=4, distance="4.1234")

    def test_get_valid_single_frontleft(self):
        response = client.get(
            reverse('frontleft_detail', kwargs={'pk': self._3.pk})
        )
        frontleft = FrontLeftDistance.objects.get(pk=self._3.pk)
        serializer = FrontLeftDistanceSerializer(frontleft)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_frontleft(self):
        response = client.get(
            reverse('frontleft_detail', kwargs={'pk': 1000})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewFrontLeftDistanceTest(TestCase):
    """ Test module for inserting a new frontleft """

    def setUp(self):
        self.valid_payload = {
            'header_secs': 1,
            'distance': 3.97
        }
        self.invalid_payload = {
            'header_secs': None,
            'distance': 1.234
        }

    def test_create_valid_frontleft(self):
        response = client.post(
            reverse('frontleft_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_frontleft(self):
        response = client.post(
            reverse('frontleft_list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleFrontLeftDistanceTest(TestCase):
    """ Test module for deleting an existing frontleft record """

    def setUp(self):
        self._1 = FrontLeftDistance.objects.create(
            header_secs=1, distance="1.1234")
        self._2 = FrontLeftDistance.objects.create(
            header_secs=2, distance="2.1234")

    def test_valid_delete_frontleft(self):
        response = client.delete(
            reverse('frontleft_detail', kwargs={'pk': self._1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_frontleft(self):
        response = client.delete(
            reverse('frontleft_detail', kwargs={'pk': 1000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)