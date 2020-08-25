'''
URL module for the imu class
'''
from django.urls import path
from mayflower_server.imu import views

urlpatterns = [
    path('', views.IMUList.as_view()),
    path('<int:pk>/', views.IMUDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
