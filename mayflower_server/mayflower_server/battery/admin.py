'''
battery admin file
'''
from django.contrib import admin
from mayflower_server.battery.models import Battery


# Register your models here.
admin.site.register(Battery)