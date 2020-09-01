from django.contrib import admin
from .models import employee
from ModelTracker.Tracker import TrackerAdmin

admin.register(employee,TrackerAdmin)