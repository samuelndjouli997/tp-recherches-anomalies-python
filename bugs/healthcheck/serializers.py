from rest_framework import serializers


class HealthCheckSerializer(serializers.Serializer):
    requestedAt = serializers.DateTimeField()
    message = serializers.CharField(max_length=255)
