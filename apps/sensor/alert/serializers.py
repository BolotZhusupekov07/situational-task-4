from rest_framework import serializers

from apps.sensor.alert.models import SensorAlert


class SensorAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorAlert
        fields = [
            "id",
            "sensor",
            "description",
            "date",
        ]
        read_only_fields = ["id"]
