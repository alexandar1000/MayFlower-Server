'''
URL module for the front left class
'''
from django.urls import path
from mayflower_server.distance.frontLeft import views

urlpatterns = [
    path('', views.FrontLeftList.as_view(), name="frontleft_list"),
    path('<int:pk>/', views.FrontLeftDetail.as_view(), name="frontleft_detail")
]
