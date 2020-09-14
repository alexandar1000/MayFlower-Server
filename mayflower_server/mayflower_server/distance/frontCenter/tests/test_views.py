import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import FrontCenterDistance
from ..serializers import FrontCenterDistanceSerializer

# Initialise the APIClient App
client = Client()

class GetAllFrontCenterTest(TestCase):
    """ Test module for GET all FrontCenterDistances API """

    def setUp(self):
        FrontCenterDistance.objects.create(
            header_secs=1, distance="4.1234")
        FrontCenterDistance.objects.create(
            header_secs=2, distance="4.1234")
        FrontCenterDistance.objects.create(
            header_secs=3, distance="4.1234")
        FrontCenterDistance.objects.create(
            header_secs=4, distance="4.1234")

    def test_get_all_frontcenter(self):
        # get API response
        response = client.get(reverse('frontcenter_list'))
        # get data from db
        frontcenter = FrontCenterDistance.objects.all()
        serializer = FrontCenterDistanceSerializer(frontcenter, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleFrontCenterDistanceTest(TestCase):
    """ Test module for GET a specific FrontCenterDistance API """

    def setUp(self):
        self._1 = FrontCenterDistance.objects.create(
            header_secs=1, distance="1.1234")
        self._2 = FrontCenterDistance.objects.create(
            header_secs=2, distance="2.1234")
        self._3 = FrontCenterDistance.objects.create(
            header_secs=3, distance="3.1234")
        self._4 = FrontCenterDistance.objects.create(
            header_secs=4, distance="4.1234")

    def test_get_valid_single_frontcenter(self):
        response = client.get(
            reverse('frontcenter_detail', kwargs={'pk': self._3.pk})
        )
        frontcenter = FrontCenterDistance.objects.get(pk=self._3.pk)
        serializer = FrontCenterDistanceSerializer(frontcenter)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_frontcenter(self):
        response = client.get(
            reverse('frontcenter_detail', kwargs={'pk': 1000})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewFrontCenterDistanceTest(TestCase):
    """ Test module for inserting a new frontcenter """

    def setUp(self):
        self.valid_payload = {
            'header_secs': 1,
            'distance': 3.97
        }
        self.invalid_payload = {
            'header_secs': None,
            'distance': 1.234
        }

    def test_create_valid_frontcenter(self):
        response = client.post(
            reverse('frontcenter_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_frontcenter(self):
        response = client.post(
            reverse('frontcenter_list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleFrontCenterDistanceTest(TestCase):
    """ Test module for deleting an existing frontcenter record """

    def setUp(self):
        self._1 = FrontCenterDistance.objects.create(
            header_secs=1, distance="1.1234")
        self._2 = FrontCenterDistance.objects.create(
            header_secs=2, distance="2.1234")

    def test_valid_delete_frontcenter(self):
        response = client.delete(
            reverse('frontcenter_detail', kwargs={'pk': self._1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_frontcenter(self):
        response = client.delete(
            reverse('frontcenter_detail', kwargs={'pk': 1000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)