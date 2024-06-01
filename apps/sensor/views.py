from rest_framework import viewsets

from apps.sensor.models import Sensor
from apps.sensor.serializers import SensorSerializer


class SensorViewSet(viewsets.ModelViewSet):
    serializer_class = SensorSerializer
    model = Sensor
    queryset = Sensor.objects.all().order_by("-title")
