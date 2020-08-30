"""mayflower_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/temperatures/', include('mayflower_server.thermometer.urls')),
    path('api/v1/controls/', include('mayflower_server.controls.urls')),
    path('api/v1/video/', include('mayflower_server.video.urls')),
    path('api/v1/battery/', include('mayflower_server.battery.urls')),
    path('api/v1/gps/', include('mayflower_server.gps.urls')),
    path('api/v1/imu/', include('mayflower_server.imu.urls')),
    path('api/v1/3DLidar/', include('mayflower_server.lidar.urls')),
    path('api/v1/frontCenter', include('mayflower_server.distance.frontCenter.urls')),
    path('api/v1/frontLeft', include('mayflower_server.distance.frontLeft.urls')),
    path('api/v1/frontRight', include('mayflower_server.distance.frontRight.urls')),
    path('api/v1/leftAngle', include('mayflower_server.distance.leftAngle.urls')),
    path('api/v1/rightAngle', include('mayflower_server.distance.rightAngle.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
