from django.test import TestCase
from ..models import Temperature


class TemperatureTest(TestCase):
    """ Test module for Temperature model """

    def setUp(self):
        Temperature.objects.create(
            header_secs=1, temperature="25")
        Temperature.objects.create(
            header_secs=2, temperature="18")

    def test_toString(self):
        distance_1 = Temperature.objects.get(header_secs=1)
        distance_2 = Temperature.objects.get(header_secs=2)
        self.assertEqual(
            str(distance_1), "25.00")
        self.assertEqual(
            str(distance_2), "18.00")
