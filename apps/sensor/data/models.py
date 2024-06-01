from django.utils import timezone
from django.db import models

from apps.sensor.models import Sensor


class SensorData(models.Model):
    sensor = models.ForeignKey(Sensor, models.CASCADE)
    pm_2_5_level = models.DecimalField(max_digits=10, decimal_places=2)
    pm_10_level = models.DecimalField(max_digits=10, decimal_places=2)
    co_2_level = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
