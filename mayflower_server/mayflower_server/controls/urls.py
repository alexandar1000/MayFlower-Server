from django.urls import path

from . import views

urlpatterns = [
    path('', views.ControlsList.as_view()),
    path('<int:pk>/', views.ControlsDetail.as_view()),
    path('command', views.control_list)
]