from rest_framework import serializers

class Serialiazer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
