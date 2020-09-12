'''
URL module for the front right class
'''
from django.urls import path
from mayflower_server.distance.frontRight import views

urlpatterns = [
    path('', views.FrontRightList.as_view(),name="frontright_list"),
    path('<int:pk>/', views.FrontRightDetail.as_view(), name="frontright_detail")
]
