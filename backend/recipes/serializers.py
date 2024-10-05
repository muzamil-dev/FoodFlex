from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(allow_blank=True)
    ingredients = serializers.CharField(allow_blank=True)  # Changed to CharField
    instructions = serializers.CharField(allow_blank=True)
    
    def create(self, validated_data):
        return Recipe(**validated_data).save()
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.ingredients = validated_data.get('ingredients', instance.ingredients)
        instance.instructions = validated_data.get('instructions', instance.instructions)
        instance.save()
        return instance
