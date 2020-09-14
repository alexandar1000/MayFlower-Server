from django.test import TestCase
from ..models import FrontRightDistance


class FrontRightDistanceTest(TestCase):
    """ Test module for FrontRightDistance model """

    def setUp(self):
        FrontRightDistance.objects.create(
            header_secs=1, distance="4.1234")
        FrontRightDistance.objects.create(
            header_secs=2, distance="9.555553")

    def test_toString(self):
        distance_1 = FrontRightDistance.objects.get(header_secs=1)
        distance_2 = FrontRightDistance.objects.get(header_secs=2)
        self.assertEqual(
            str(distance_1), "4.1234")
        self.assertEqual(
            str(distance_2), "9.555553")
