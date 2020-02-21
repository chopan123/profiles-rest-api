from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testiting  our ApiView"""
    name = serializers.CharField(max_length=10)
