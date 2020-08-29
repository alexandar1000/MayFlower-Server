'''
URL module for the front left class
'''
from django.urls import path
from mayflower_server.distance.frontLeft import views

urlpatterns = [
    path('', views.FrontLeftList.as_view()),
    path('<int:pk>/', views.FrontLeftDetail.as_view())
]
