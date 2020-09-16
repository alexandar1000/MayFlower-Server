import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Battery
from ..serializers import BatterySerializer

# Initialise the APIClient App
client = Client()

class GetAllBatteriesTest(TestCase):
    """ Test module for GET all Batterys API """
    def setUp(self):
        Battery.objects.create(
            header_secs=1, percentage=98.70, power_supply_status="DISCHARGING")
        Battery.objects.create(
            header_secs=2, percentage=56.70, power_supply_status="CHARGING")
        Battery.objects.create(
            header_secs=3, percentage=45.31, power_supply_status="DISCHARGING")
        Battery.objects.create(
            header_secs=4, percentage=60.70, power_supply_status="CHARGING")

    def test_get_all_battery(self):
        # get API response
        response = client.get(reverse('battery_list'))
        # get data from db
        battery = Battery.objects.all()
        serializer = BatterySerializer(battery, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleBatteryTest(TestCase):
    """ Test module for GET a specific Battery API """

    def setUp(self):
        self._1 = Battery.objects.create(
            header_secs=1, percentage=18.70, power_supply_status="DISCHARGING")
        self._2 = Battery.objects.create(
            header_secs=2, percentage=28.70, power_supply_status="DISCHARGING")
        self._3 = Battery.objects.create(
            header_secs=3, percentage=38.70, power_supply_status="DISCHARGING")
        self._4 = Battery.objects.create(
            header_secs=4, percentage=48.70, power_supply_status="DISCHARGING")

    def test_get_valid_single_battery(self):
        response = client.get(
            reverse('battery_detail', kwargs={'pk': self._3.pk})
        )
        battery = Battery.objects.get(pk=self._3.pk)
        serializer = BatterySerializer(battery)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_battery(self):
        response = client.get(
            reverse('battery_detail', kwargs={'pk': 1000})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewBatteryTest(TestCase):
    """ Test module for inserting a new battery """

    def setUp(self):
        self.valid_payload = {
            'header_secs': 1,
            'percentage': 30.97,
            'power_supply_status': "DISCHARGING"
        }
        self.invalid_payload = {
            'header_secs': None,
            'percentage': 30.97,
            'power_supply_status': "DISCHARGING"
        }

    def test_create_valid_battery(self):
        response = client.post(
            reverse('battery_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_battery(self):
        response = client.post(
            reverse('battery_list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleBatteryTest(TestCase):
    """ Test module for updating an existing Battery record """

    def setUp(self):
        self._1 = Battery.objects.create(
            header_secs=1, percentage=60.70, power_supply_status="CHARGING")
        self._2 = Battery.objects.create(
            header_secs=2, percentage=60.70, power_supply_status="CHARGING")
        self.valid_payload = {
            'header_secs': 1,
            'percentage': 30.97,
            'power_supply_status': "DISCHARGING"
        }
        self.invalid_payload = {
            'header_secs': None,
            'percentage': 30.97,
            'power_supply_status': "DISCHARGING"
        }

    def test_valid_update_battery(self):
        response = client.put(
            reverse('battery_detail', kwargs={'pk': self._1.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_battery(self):
        response = client.put(
            reverse('battery_detail', kwargs={'pk': self._1.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleBatteryTest(TestCase):
    """ Test module for deleting an existing battery record """

    def setUp(self):
        self._1 = Battery.objects.create(
            header_secs=1, percentage=60.70, power_supply_status="CHARGING")
        self._2 = Battery.objects.create(
            header_secs=2, percentage=60.70, power_supply_status="CHARGING")

    def test_valid_delete_battery(self):
        response = client.delete(
            reverse('battery_detail', kwargs={'pk': self._1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_battery(self):
        response = client.delete(
            reverse('battery_detail', kwargs={'pk': 1000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)