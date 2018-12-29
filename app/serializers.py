from rest_framework import serializers
from app.models import Alert

class AlertSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(required=False, allow_blank=True)
    latitude = serializers.DecimalField(max_digits=8, decimal_places=4)
    longitude = serializers.DecimalField(max_digits=8, decimal_places=4)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new 'Alert' instance, given the validated data.
        """
        return Alert.objects.create(**validated_data)

class AlertUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(required=False, max_length=100)
    description = serializers.CharField(required=False, allow_blank=True)
    latitude = serializers.DecimalField(max_digits=8, decimal_places=4, required=False)
    longitude = serializers.DecimalField(max_digits=8, decimal_places=4, required=False)
     
    def update(self, instance, validated_data):
        """
        Update and return an existing 'Alert' instance, given the validated
        data
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',
                instance.description)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.save()
        return instance

