from django.test import TestCase
from ..models import LeftAngleDistance


class LeftAngleDistanceTest(TestCase):
    """ Test module for LeftAngleDistance model """

    def setUp(self):
        LeftAngleDistance.objects.create(
            header_secs=1, distance="4.1234")
        LeftAngleDistance.objects.create(
            header_secs=2, distance="9.555553")

    def test_toString(self):
        distance_1 = LeftAngleDistance.objects.get(header_secs=1)
        distance_2 = LeftAngleDistance.objects.get(header_secs=2)
        self.assertEqual(
            str(distance_1), "4.1234")
        self.assertEqual(
            str(distance_2), "9.555553")
