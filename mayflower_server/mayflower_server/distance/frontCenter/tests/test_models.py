from django.test import TestCase
from ..models import FrontCenterDistance


class FrontCenterDistanceTest(TestCase):
    """ Test module for FrontCenterDistance model """

    def setUp(self):
        FrontCenterDistance.objects.create(
            header_secs=1, distance="4.1234")
        FrontCenterDistance.objects.create(
            header_secs=2, distance="9.555553")

    def test_toString(self):
        distance_1 = FrontCenterDistance.objects.get(header_secs=1)
        distance_2 = FrontCenterDistance.objects.get(header_secs=2)
        self.assertEqual(
            str(distance_1), "4.1234")
        self.assertEqual(
            str(distance_2), "9.555553")
