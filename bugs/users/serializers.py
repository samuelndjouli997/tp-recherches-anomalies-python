from rest_framework import serializers


class UsersSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=90)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    state = serializers.CharField(max_length=255)
    postcode = serializers.CharField(max_length=255)
    is_active = serializers.BooleanField()
