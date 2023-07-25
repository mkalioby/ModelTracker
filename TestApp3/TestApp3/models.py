from django.db import models

from ModelTracker import Tracker

class employee(Tracker.ModelTracker):
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    age=models.IntegerField()

