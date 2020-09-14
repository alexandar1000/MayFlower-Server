from django.test import TestCase
from ..models import FrontLeftDistance


class FrontLeftDistanceTest(TestCase):
    """ Test module for FrontLeftDistance model """

    def setUp(self):
        FrontLeftDistance.objects.create(
            header_secs=1, distance="4.1234")
        FrontLeftDistance.objects.create(
            header_secs=2, distance="9.555553")

    def test_toString(self):
        distance_1 = FrontLeftDistance.objects.get(header_secs=1)
        distance_2 = FrontLeftDistance.objects.get(header_secs=2)
        self.assertEqual(
            str(distance_1), "4.1234")
        self.assertEqual(
            str(distance_2), "9.555553")
