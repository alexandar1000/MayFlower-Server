from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from mayflower_server.thermometer.models import Temperature
from mayflower_server.thermometer.serializers import TemperatureSerializer
from .ros_listen import RosTemperatureListener

ros_client = RosTemperatureListener(ros_host='localhost')

class TemperatureList(APIView):
    """
    List all temeratures, or create a new temperature reading.
    """
    def get(self, request):
        temperatures = Temperature.objects.all()
        serializer = TemperatureSerializer(temperatures, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TemperatureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TemperatureDetail(APIView):
    """
    Retrieve, update or delete a temperature reading.
    """
    def get_object(self, pk):
        try:
            return Temperature.objects.get(pk=pk)
        except Temperature.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        temperature = self.get_object(pk)
        serializer = TemperatureSerializer(temperature)
        return Response(serializer.data)

    def delete(self, request, pk):
        temperature = self.get_object(pk)
        temperature.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)