import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Temperature
from ..serializers import TemperatureSerializer

# Initialise the APIClient App
client = Client()

class GetAllFrontCenterTest(TestCase):
    """ Test module for GET all Temperatures API """

    def setUp(self):
        Temperature.objects.create(
            header_secs=1, temperature="11")
        Temperature.objects.create(
            header_secs=2, temperature="12")
        Temperature.objects.create(
            header_secs=3, temperature="13")
        Temperature.objects.create(
            header_secs=4, temperature="14")

    def test_get_all_temperature(self):
        # get API response
        response = client.get(reverse('temperature_list'))
        # get data from db
        temperature = Temperature.objects.all()
        serializer = TemperatureSerializer(temperature, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleTemperatureTest(TestCase):
    """ Test module for GET a specific Temperature API """

    def setUp(self):
        self._1 = Temperature.objects.create(
            header_secs=1, temperature="25")
        self._2 = Temperature.objects.create(
            header_secs=2, temperature="26")
        self._3 = Temperature.objects.create(
            header_secs=3, temperature="27")
        self._4 = Temperature.objects.create(
            header_secs=4, temperature="28")

    def test_get_valid_single_temperature(self):
        response = client.get(
            reverse('temperature_detail', kwargs={'pk': self._3.pk})
        )
        temperature = Temperature.objects.get(pk=self._3.pk)
        serializer = TemperatureSerializer(temperature)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_temperature(self):
        response = client.get(
            reverse('temperature_detail', kwargs={'pk': 1000})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewTemperatureTest(TestCase):
    """ Test module for inserting a new temperature """

    def setUp(self):
        self.valid_payload = {
            'header_secs': 1,
            'temperature': 25
        }
        self.invalid_payload = {
            'header_secs': None,
            'temperature': 25
        }

    def test_create_valid_temperature(self):
        response = client.post(
            reverse('temperature_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_temperature(self):
        response = client.post(
            reverse('temperature_list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleTemperatureTest(TestCase):
    """ Test module for deleting an existing temperature record """

    def setUp(self):
        self._1 = Temperature.objects.create(
            header_secs=1, temperature="16")
        self._2 = Temperature.objects.create(
            header_secs=2, temperature="17")

    def test_valid_delete_temperature(self):
        response = client.delete(
            reverse('temperature_detail', kwargs={'pk': self._1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_temperature(self):
        response = client.delete(
            reverse('temperature_detail', kwargs={'pk': 1000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)