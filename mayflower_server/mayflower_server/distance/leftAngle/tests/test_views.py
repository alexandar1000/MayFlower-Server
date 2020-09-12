import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import LeftAngleDistance
from ..serializers import LeftAngleDistanceSerializer

# Initialise the APIClient App
client = Client()

class GetAllLeftAngleTest(TestCase):
    """ Test module for GET all LeftAngleDistances API """

    def setUp(self):
        LeftAngleDistance.objects.create(
            header_secs=1, distance="4.1234")
        LeftAngleDistance.objects.create(
            header_secs=2, distance="4.1234")
        LeftAngleDistance.objects.create(
            header_secs=3, distance="4.1234")
        LeftAngleDistance.objects.create(
            header_secs=4, distance="4.1234")

    def test_get_all_leftangle(self):
        # get API response
        response = client.get(reverse('leftangle_list'))
        # get data from db
        leftangle = LeftAngleDistance.objects.all()
        serializer = LeftAngleDistanceSerializer(leftangle, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleLeftAngleDistanceTest(TestCase):
    """ Test module for GET a specific LeftAngleDistance API """

    def setUp(self):
        self._1 = LeftAngleDistance.objects.create(
            header_secs=1, distance="1.1234")
        self._2 = LeftAngleDistance.objects.create(
            header_secs=2, distance="2.1234")
        self._3 = LeftAngleDistance.objects.create(
            header_secs=3, distance="3.1234")
        self._4 = LeftAngleDistance.objects.create(
            header_secs=4, distance="4.1234")

    def test_get_valid_single_leftangle(self):
        response = client.get(
            reverse('leftangle_detail', kwargs={'pk': self._3.pk})
        )
        leftangle = LeftAngleDistance.objects.get(pk=self._3.pk)
        serializer = LeftAngleDistanceSerializer(leftangle)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_leftangle(self):
        response = client.get(
            reverse('leftangle_detail', kwargs={'pk': 1000})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewLeftAngleDistanceTest(TestCase):
    """ Test module for inserting a new leftangle """

    def setUp(self):
        self.valid_payload = {
            'header_secs': 1,
            'distance': 3.97
        }
        self.invalid_payload = {
            'header_secs': None,
            'distance': 1.234
        }

    def test_create_valid_leftangle(self):
        response = client.post(
            reverse('leftangle_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_leftangle(self):
        response = client.post(
            reverse('leftangle_list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleLeftAngleDistanceTest(TestCase):
    """ Test module for deleting an existing leftangle record """

    def setUp(self):
        self._1 = LeftAngleDistance.objects.create(
            header_secs=1, distance="1.1234")
        self._2 = LeftAngleDistance.objects.create(
            header_secs=2, distance="2.1234")

    def test_valid_delete_leftangle(self):
        response = client.delete(
            reverse('leftangle_detail', kwargs={'pk': self._1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_leftangle(self):
        response = client.delete(
            reverse('leftangle_detail', kwargs={'pk': 1000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)