'''
URL module for the battery class
'''
from django.urls import path
from mayflower_server.battery import views

urlpatterns = [
    path('', views.BatteryList.as_view(), name="battery_list"),
    path('<int:pk>/', views.BatteryDetail.as_view(), name="battery_detail"),
    path('current/', views.BatteryCurrent.as_view(), name="battery_current")
]

# urlpatterns = format_suffix_patterns(urlpatterns)
