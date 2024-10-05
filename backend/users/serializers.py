from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from mongoengine.errors import NotUniqueError

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    religious_restrictions = serializers.ChoiceField(
        choices=User.RELIGIOUS_RESTRICTIONS_OPTIONS,
        default='None',
        required=False
    )
    diet = serializers.ChoiceField(
        choices=User.DIET_OPTIONS,
        default='None',
        required=False
    )
    allergies = serializers.ListField(
        child=serializers.ChoiceField(choices=User.ALLERGY_OPTIONS),
        default=[],
        required=False
    )

    def create(self, validated_data):
        # Hash the password before saving
        validated_data['password'] = make_password(validated_data['password'])
        try:
            # Try to create a new user with validated data
            user = User(**validated_data)
            user.save()  # This will raise NotUniqueError if email is already used
            return user
        except NotUniqueError:
            raise serializers.ValidationError({"email": "A user with this email already exists."})

    def validate(self, data):
        # Any other custom validation logic can go here
        return data
    
import re


class UserDietSerializer(serializers.Serializer):
    diet = serializers.ChoiceField(choices=User.DIET_OPTIONS)

    def update(self, instance, validated_data):
        instance.religious_restrictions = validated_data.get('religious_restrictions', instance.religious_restrictions)
        instance.diet = validated_data.get('diet', instance.diet)
        instance.allergies = validated_data.get('allergies', instance.allergies)
        instance.save()
        return instance