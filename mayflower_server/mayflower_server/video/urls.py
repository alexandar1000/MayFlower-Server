'''
URL module for the video feed class
'''
from django.urls import path
from mayflower_server.video import views

urlpatterns = [
    # path('', views.VideoFeedList.as_view()),
    path('<int:pk>/', views.VideoFeedDetail.as_view()),
    path('', views.ImageFeedDetail.as_view())
]