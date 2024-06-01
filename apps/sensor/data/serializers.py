from rest_framework import serializers

from apps.sensor.data.models import SensorData


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = [
            "id",
            "sensor",
            "pm_2_5_level",
            "pm_10_level",
            "co_2_level",
            "date",
        ]
        read_only_fields = ["id", "date"]
