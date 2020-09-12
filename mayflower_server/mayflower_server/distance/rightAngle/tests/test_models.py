from django.test import TestCase
from ..models import RightAngleDistance


class RightAngleDistanceTest(TestCase):
    """ Test module for RightAngleDistance model """

    def setUp(self):
        RightAngleDistance.objects.create(
            header_secs=1, distance="4.1234")
        RightAngleDistance.objects.create(
            header_secs=2, distance="9.555553")

    def test_toString(self):
        distance_1 = RightAngleDistance.objects.get(header_secs=1)
        distance_2 = RightAngleDistance.objects.get(header_secs=2)
        self.assertEqual(
            str(distance_1), "4.1234")
        self.assertEqual(
            str(distance_2), "9.555553")
