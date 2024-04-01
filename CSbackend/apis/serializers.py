from rest_framework import serializers


class MovieDetailSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    id = serializers.IntegerField(required=False)