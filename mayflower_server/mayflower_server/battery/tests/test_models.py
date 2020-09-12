from django.test import TestCase
from ..models import Battery


class BatteryTest(TestCase):
    """ Test module for Battery model """

    def setUp(self):
        Battery.objects.create(
            header_secs=1, percentage=98.70, power_supply_status="DISCHARGING")
        Battery.objects.create(
            header_secs=2, percentage=56.70, power_supply_status="CHARGING")

    def test_toString(self):
        battery_1 = Battery.objects.get(header_secs=1)
        battery_2 = Battery.objects.get(header_secs=2)
        self.assertEqual(
            str(battery_1), "98.7")
        self.assertEqual(
            str(battery_2), "56.7")
