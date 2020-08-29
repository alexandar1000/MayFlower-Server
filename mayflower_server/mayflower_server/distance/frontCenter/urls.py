'''
URL module for the front center class
'''
from django.urls import path
from mayflower_server.distance.frontCenter import views

urlpatterns = [
    path('', views.FrontCenterList.as_view()),
    path('<int:pk>/', views.FrontCenterDetail.as_view())
]
