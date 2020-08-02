from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from mayflower_server.thermometer import views

urlpatterns = [
    path('', views.TemperatureList.as_view()),
    path('<int:pk>/', views.TemperatureDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)