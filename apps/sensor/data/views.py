from rest_framework import viewsets

from apps.sensor.data.models import SensorData
from apps.sensor.data.serializers import SensorDataSerializer
from django_filters.rest_framework import DjangoFilterBackend


class SensorDataViewSet(viewsets.ModelViewSet):
    serializer_class = SensorDataSerializer
    model = SensorData
    queryset = SensorData.objects.all().order_by("-date")
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["sensor"]
