from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    ingredients = serializers.ListField(child=serializers.CharField())

    # This is optional but useful if you want to save data
    def create(self, validated_data):
        return Recipe(**validated_data)
