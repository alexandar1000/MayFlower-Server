import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import FrontRightDistance
from ..serializers import FrontRightDistanceSerializer

# Initialise the APIClient App
client = Client()

class GetAllFrontRightTest(TestCase):
    """ Test module for GET all FrontRightDistances API """

    def setUp(self):
        FrontRightDistance.objects.create(
            header_secs=1, distance="4.1234")
        FrontRightDistance.objects.create(
            header_secs=2, distance="4.1234")
        FrontRightDistance.objects.create(
            header_secs=3, distance="4.1234")
        FrontRightDistance.objects.create(
            header_secs=4, distance="4.1234")

    def test_get_all_frontright(self):
        # get API response
        response = client.get(reverse('frontright_list'))
        # get data from db
        frontright = FrontRightDistance.objects.all()
        serializer = FrontRightDistanceSerializer(frontright, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleFrontRightDistanceTest(TestCase):
    """ Test module for GET a specific FrontRightDistance API """

    def setUp(self):
        self._1 = FrontRightDistance.objects.create(
            header_secs=1, distance="1.1234")
        self._2 = FrontRightDistance.objects.create(
            header_secs=2, distance="2.1234")
        self._3 = FrontRightDistance.objects.create(
            header_secs=3, distance="3.1234")
        self._4 = FrontRightDistance.objects.create(
            header_secs=4, distance="4.1234")

    def test_get_valid_single_frontright(self):
        response = client.get(
            reverse('frontright_detail', kwargs={'pk': self._3.pk})
        )
        frontright = FrontRightDistance.objects.get(pk=self._3.pk)
        serializer = FrontRightDistanceSerializer(frontright)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_frontright(self):
        response = client.get(
            reverse('frontright_detail', kwargs={'pk': 1000})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewFrontRightDistanceTest(TestCase):
    """ Test module for inserting a new frontright """

    def setUp(self):
        self.valid_payload = {
            'header_secs': 1,
            'distance': 3.97
        }
        self.invalid_payload = {
            'header_secs': None,
            'distance': 1.234
        }

    def test_create_valid_frontright(self):
        response = client.post(
            reverse('frontright_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_frontright(self):
        response = client.post(
            reverse('frontright_list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleFrontRightDistanceTest(TestCase):
    """ Test module for deleting an existing frontright record """

    def setUp(self):
        self._1 = FrontRightDistance.objects.create(
            header_secs=1, distance="1.1234")
        self._2 = FrontRightDistance.objects.create(
            header_secs=2, distance="2.1234")

    def test_valid_delete_frontright(self):
        response = client.delete(
            reverse('frontright_detail', kwargs={'pk': self._1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_frontright(self):
        response = client.delete(
            reverse('frontright_detail', kwargs={'pk': 1000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)