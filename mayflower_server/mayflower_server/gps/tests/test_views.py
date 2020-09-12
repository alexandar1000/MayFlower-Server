import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import GPS
from ..serializers import GPSSerializer


# Initialise the APIClient App
client = Client()

class GetAllGPSsTest(TestCase):
    """ Test module for GET all GPSs API """

    def setUp(self):
        GPS.objects.create(
            header_secs=1, latitude=1.999, longitude=-2.0001, altitude=10)
        GPS.objects.create(
            header_secs=2, latitude=2.999, longitude=-2.0001, altitude=10)
        GPS.objects.create(
            header_secs=3, latitude=3.999, longitude=-2.0001, altitude=10)
        GPS.objects.create(
            header_secs=4, latitude=4.999, longitude=-2.0001, altitude=10)

    def test_get_all_gps(self):
        # get API response
        response = client.get(reverse('gps_list'))
        # get data from db
        gps = GPS.objects.all()
        serializer = GPSSerializer(gps, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleGPSTest(TestCase):
    """ Test module for GET a specific GPS API """

    def setUp(self):
        self._1 = GPS.objects.create(
            header_secs=1, latitude=1.999, longitude=-2.0001, altitude=10)
        self._2 = GPS.objects.create(
            header_secs=2, latitude=2.999, longitude=-2.0001, altitude=10)
        self._3 = GPS.objects.create(
            header_secs=3, latitude=3.999, longitude=-2.0001, altitude=10)
        self._4 = GPS.objects.create(
            header_secs=4, latitude=4.999, longitude=-2.0001, altitude=10)

    def test_get_valid_single_gps(self):
        response = client.get(
            reverse('gps_detail', kwargs={'pk': self._3.pk})
        )
        gps = GPS.objects.get(pk=self._3.pk)
        serializer = GPSSerializer(gps)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_gps(self):
        response = client.get(
            reverse('gps_detail', kwargs={'pk': 1000})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewGPSTest(TestCase):
    """ Test module for inserting a new gps """

    def setUp(self):
        self.valid_payload = {
            'header_secs': 1,
            'latitude': 1.999,
            'longitude': -2.0001,
            'altitude': 10
        }
        self.invalid_payload = {
            'header_secs': None,
            'latitude': 1.999,
            'longitude': -2.0001,
            'altitude': 10
        }

    def test_create_valid_gps(self):
        response = client.post(
            reverse('gps_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_gps(self):
        response = client.post(
            reverse('gps_list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleGPSTest(TestCase):
    """ Test module for updating an existing GPS record """

    def setUp(self):
        self._1 = GPS.objects.create(
            header_secs=1, latitude=1.999, longitude=-2.0001, altitude=10)
        self._2 = GPS.objects.create(
            header_secs=2, latitude=2.999, longitude=-2.0001, altitude=10)
        self.valid_payload = {
            'header_secs': 1,
            'latitude': 10.999,
            'longitude': -20.0001,
            'altitude': 1
        }
        self.invalid_payload = {
            'header_secs': None,
            'latitude': 1.999,
            'longitude': -2.0001,
            'altitude': 10
        }

    def test_valid_update_gps(self):
        response = client.put(
            reverse('gps_detail', kwargs={'pk': self._1.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_gps(self):
        response = client.put(
            reverse('gps_detail', kwargs={'pk': self._1.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleGPSTest(TestCase):
    """ Test module for deleting an existing gps record """

    def setUp(self):
        self._1 = GPS.objects.create(
            header_secs=1, latitude=1.999, longitude=-2.0001, altitude=10)
        self._2 = GPS.objects.create(
            header_secs=2, latitude=2.999, longitude=-2.0001, altitude=10)

    def test_valid_delete_gps(self):
        response = client.delete(
            reverse('gps_detail', kwargs={'pk': self._1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_gps(self):
        response = client.delete(
            reverse('gps_detail', kwargs={'pk': 1000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# Additional API
# class GetGPSSetByTimeTest(TestCase):
#     """ Test module for retrieving a set of GPSs created in some time """
#
#     def setUp(self):
#         GPS.objects.create(
#             header_secs=1, latitude=1.999, longitude=-2.0001, altitude=10)
#         GPS.objects.create(
#             header_secs=2, latitude=2.999, longitude=-2.0001, altitude=10)
#         GPS.objects.create(
#             header_secs=3, latitude=3.999, longitude=-2.0001, altitude=10)
#         GPS.objects.create(
#             header_secs=4, latitude=4.999, longitude=-2.0001, altitude=10)
#         GPS.objects.create(
#             header_secs=5, latitude=1.999, longitude=-2.0001, altitude=10)
#         GPS.objects.create(
#             header_secs=6, latitude=2.999, longitude=-2.0001, altitude=10)
#         GPS.objects.create(
#             header_secs=7, latitude=3.999, longitude=-2.0001, altitude=10)
#         GPS.objects.create(
#             header_secs=8, latitude=4.999, longitude=-2.0001, altitude=10)
#
#     def test_valid_get_gps_by_time(self):
#         response = client.get(
#             reverse('gps_list', kwargs={'min_header_secs': 3, 'max_header_secs': 7}))
#         # get data from db
#         gpsQueryset = GPS.objects.filter(header_secs__gte=3, header_secs__lte=7)
#         serializer = GPSSerializer(gpsQueryset)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, serializer.data)