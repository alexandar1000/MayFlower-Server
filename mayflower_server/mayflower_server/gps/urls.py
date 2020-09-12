'''
URL module for the gps class
'''
from django.urls import path
from mayflower_server.gps import views

urlpatterns = [
    path('', views.GPSList.as_view(), name="gps_list"),
    path('<int:pk>/', views.GPSDetail.as_view(), name="gps_detail")
]
