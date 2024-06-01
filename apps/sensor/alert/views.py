from rest_framework import viewsets

from apps.sensor.alert.models import SensorAlert
from apps.sensor.alert.serializers import SensorAlertSerializer
from django_filters.rest_framework import DjangoFilterBackend


class SensorAlertViewSet(viewsets.ModelViewSet):
    serializer_class = SensorAlertSerializer
    model = SensorAlert
    queryset = SensorAlert.objects.all().order_by("-date")
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["sensor"]
