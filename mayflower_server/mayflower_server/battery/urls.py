'''
URL module for the battery class
'''
from django.urls import path
from mayflower_server.battery import views

urlpatterns = [
    path('', views.BatteryPowerList.as_view()),
    path('<int:pk>/', views.BatteryPowerDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
