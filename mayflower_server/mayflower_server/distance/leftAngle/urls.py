'''
URL module for the front left class
'''
from django.urls import path
from mayflower_server.distance.leftAngle import views

urlpatterns = [
    path('', views.LeftAngleList.as_view()),
    path('<int:pk>/', views.LeftAngleDetail.as_view())
]
