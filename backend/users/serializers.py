import re
from rest_framework import serializers
from .models import User

class UserDietSerializer(serializers.Serializer):
    diet = serializers.ChoiceField(choices=User.DIET_CHOICES)

    def update(self, instance, validated_data):
        instance.diet = validated_data.get('diet', instance.diet)
        instance.save()
        return instance