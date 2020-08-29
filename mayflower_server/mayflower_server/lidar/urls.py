'''
URL module for the lidar class
'''
from django.urls import path
from mayflower_server.lidar import views

urlpatterns = [
    path('', views.Lidar3DList.as_view()),
    path('<int:pk>/', views.Lidar3DDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
