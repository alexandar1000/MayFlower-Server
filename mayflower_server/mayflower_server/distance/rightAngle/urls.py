'''
URL module for the right angle class
'''
from django.urls import path
from mayflower_server.distance.rightAngle import views

urlpatterns = [
    path('', views.RightAngleList.as_view(),name="rightangle_list"),
    path('<int:pk>/', views.RightAngleDetail.as_view(), name="rightangle_detail")
]
