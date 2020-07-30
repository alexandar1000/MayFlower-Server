from rest_framework import generics

from .models import Controls
from .serializers import ControlsSerializer

from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from .ros_publish import RosControlsPublisher
from ..scripts import ros_connection

ros_client = ros_connection.init_client()

# Create your views here.
class ControlsList(generics.ListAPIView):
    queryset = Controls.objects.all()
    serializer_class = ControlsSerializer


class ControlsDetail(generics.RetrieveUpdateAPIView):
    queryset = Controls.objects.all()
    serializer_class = ControlsSerializer


@api_view(['POST'])
def control_list(request):
    command_data = JSONParser().parse(request)
    # print(command_data)
    command_serializer = ControlsSerializer(data=command_data)
    # print(command_serializer)
    if command_serializer.is_valid():
        command_serializer.save()
        result = ros_client.send_command(command_data['command'])
        if result:
            return JsonResponse(command_serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return JsonResponse(command_serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)

    return JsonResponse(command_serializer.data, status=status.HTTP_400_BAD_REQUEST)


