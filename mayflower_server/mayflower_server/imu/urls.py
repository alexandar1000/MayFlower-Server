'''
URL module for the imu class
'''
from django.urls import path
from mayflower_server.imu import views

urlpatterns = [
    path('', views.IMUList.as_view(), name="imu_list"),
    path('<int:pk>/', views.IMUDetail.as_view(), name="imu_detail"),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
