from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from mayflower_server.thermometer import views

urlpatterns = [
    path('', views.temperature_list),
    path('<int:pk>/', views.temperature_entry),
]

# urlpatterns = format_suffix_patterns(urlpatterns)