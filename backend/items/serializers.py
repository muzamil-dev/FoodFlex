from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField(max_length=255)
    safe = serializers.BooleanField(default=False)

    def create(self, validated_data):
        # Create and save a new Item instance
        item = Item(**validated_data)
        item.save()
        return item

    def update(self, instance, validated_data):
        # Update the Item instance
        instance.title = validated_data.get('title', instance.title)
        instance.safe = validated_data.get('safe', instance.safe)
        instance.save()
        return instance
