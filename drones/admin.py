from django.contrib import admin
import drones

from .models import DroneCategory, Drone, Pilot, Competition
# Register your models here.

admin.site.register(DroneCategory)
admin.site.register(Drone)
admin.site.register(Pilot)
admin.site.register(Competition)