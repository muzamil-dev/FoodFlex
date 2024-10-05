from rest_framework import serializers
from .models import User, Recipe
from django.contrib.auth.hashers import make_password
from mongoengine.errors import NotUniqueError
from bson.objectid import ObjectId


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
    
# add recipe id to user's favorite recipes
class AddFavoriteRecipeSerializer(serializers.Serializer):
    user_id = serializers.CharField(required=True)
    recipe_id = serializers.CharField(required=True)

    def validate_user_id(self, value):
        if not ObjectId.is_valid(value):
            raise serializers.ValidationError("Invalid user ID format.")
        if not User.objects(id=value).first():
            raise serializers.ValidationError("User does not exist.")
        return value

    def validate_recipe_id(self, value):
        if not ObjectId.is_valid(value):
            raise serializers.ValidationError("Invalid recipe ID format.")
        if not Recipe.objects(id=value).first():
            raise serializers.ValidationError("Recipe does not exist.")
        return value
    

class RemoveFavoriteRecipeSerializer(serializers.Serializer):
    user_id = serializers.CharField(required=True)
    recipe_id = serializers.CharField(required=True)

    def validate_user_id(self, value):
        if not ObjectId.is_valid(value):
            raise serializers.ValidationError("Invalid user ID format.")
        if not User.objects(id=value).first():
            raise serializers.ValidationError("User does not exist.")
        return value

    def validate_recipe_id(self, value):
        if not ObjectId.is_valid(value):
            raise serializers.ValidationError("Invalid recipe ID format.")
        if not Recipe.objects(id=value).first():
            raise serializers.ValidationError("Recipe does not exist.")
        return value
    

class RecipeSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField(allow_blank=True, required=False)
    ingredients = serializers.CharField()
    instructions = serializers.CharField()