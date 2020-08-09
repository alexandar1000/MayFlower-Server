from rest_framework import generics

from .models import Control
from .serializers import ControlsSerializer

from datetime import datetime
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from .ros_publish import RosControlPublisher
import logging

logger = logging.getLogger(__name__)

control_node = RosControlPublisher()

# Create your views here.
class ControlsList(generics.ListAPIView):
    queryset = Control.objects.all()
    serializer_class = ControlsSerializer


class ControlsDetail(generics.RetrieveUpdateAPIView):
    queryset = Control.objects.all()
    serializer_class = ControlsSerializer


@api_view(['POST'])
def control_list(request):
    command_data = JSONParser().parse(request)
    command_serializer = ControlsSerializer(data=command_data)
    if command_serializer.is_valid():
        command_serializer.save()
        result = control_node.send_command(command_data['command'])
        if result:
            return JsonResponse(command_serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            logger.warning(f"Command {command_data['command']} was not sent to ROS")
            return JsonResponse(command_serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)

    logger.warning(f"Invalid control command({command_data['command']}) post request")
    return JsonResponse(command_serializer.data, status=status.HTTP_400_BAD_REQUEST)


