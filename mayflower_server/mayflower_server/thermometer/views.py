from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mayflower_server.thermometer.models import Temperature
from mayflower_server.thermometer.serializers import TemperatureSerializer


@api_view(['GET', 'POST'])
def temperature_list(request):
    """
    List all temeratures, or create a new temperature reading.
    """
    if request.method == 'GET':
        temperatures = Temperature.objects.all()
        serializer = TemperatureSerializer(temperatures, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TemperatureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def temperature_entry(request, pk):
    """
    Retrieve, update or delete a temperature reading.
    """
    try:
        temperature = Temperature.objects.get(pk=pk)
    except Temperature.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TemperatureSerializer(temperature)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        temperature.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)