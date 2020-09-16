import django_filters

from .models import GPS

class GPSFilter(django_filters.rest_framework.FilterSet):
    """
    Filter of GPS information
    """
    min_header_secs = django_filters.NumberFilter(name="header_secs", lookup_type='gte')
    max_header_secs = django_filters.NumberFilter(name="header_secs", lookup_type='lte')
    class Meta:
        model = GPS
        fields = ['min_header_secs', 'max_header_secs']