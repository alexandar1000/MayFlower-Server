'''
URL module for the thermometer class
'''
from django.urls import path
from mayflower_server.thermometer import views

urlpatterns = [
    path('', views.TemperatureList.as_view()),
    path('<int:pk>/', views.TemperatureDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
