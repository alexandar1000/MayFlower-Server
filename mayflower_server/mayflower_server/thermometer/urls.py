'''
URL module for the thermometer class
'''
from django.urls import path
from mayflower_server.thermometer import views

urlpatterns = [
    path('', views.TemperatureList.as_view(), name="temperature_list"),
    path('<int:pk>/', views.TemperatureDetail.as_view(), name="temperature_detail"),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
