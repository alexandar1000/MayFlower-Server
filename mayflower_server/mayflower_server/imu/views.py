'''
Views for the imu package.
'''
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from mayflower_server.imu.models import IMU
from mayflower_server.imu.serializers import IMUSerializer
from .ros_listen import RosIMUListener
import logging

logger = logging.getLogger(__name__)
ros_client = RosIMUListener()


class IMUList(APIView):
    """
    List all imus, or create a new imu reading.
    """
    def get(self, request):
        '''
        Return all the imuData entries.
        '''
        imu = IMU.objects.all()
        serializer = IMUSerializer(imu, many=True)
        return Response(serializer.data)

    def post(self, request):
        '''
        Post a new IMUData entry.
        '''
        serializer = IMUSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        logger.warning("Invalid IMUData post request")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IMUDetail(APIView):
    """
    Retrieve, update or delete an imuData.
    """

    def get_object(self, primary_key):
        '''
        Retrieve the imuData db object with the primary key primary_key.
        '''
        try:
            return IMU.objects.get(pk=primary_key)
        except IMU.DoesNotExist:
            logger.error("Invalid IMUData request")
            raise Http404

    def get(self, request, pk):
        '''
        Return the IMUData with the primary key primary_key.
        '''
        imu = self.get_object(pk)
        serializer = IMUSerializer(imu)
        return Response(serializer.data)

    def delete(self, request, pk):
        '''
        Delete the IMU with the primary key primary_key.
        '''
        imu = self.get_object(pk)
        imu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
