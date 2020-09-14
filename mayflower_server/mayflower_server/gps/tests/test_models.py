from django.test import TestCase
from ..models import GPS


class GPSTest(TestCase):
    """ Test module for GPS model """

    def setUp(self):
        GPS.objects.create(
            header_secs=1, latitude=1.999, longitude=-2.0001, altitude=10)
        GPS.objects.create(
            header_secs=2, latitude=-1.999, longitude=2.0001, altitude=-10)

    def test_toString(self):
        gps_1 = GPS.objects.get(header_secs=1)
        gps_2 = GPS.objects.get(header_secs=2)
        self.assertEqual(
            str(gps_1), "(1.99900000, -2.00010000, 10.00000000)")
        self.assertEqual(
            str(gps_2), "(-1.99900000, 2.00010000, -10.00000000)")
