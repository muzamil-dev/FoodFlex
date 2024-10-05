from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Comment out or remove the import of Django's User model to avoid conflicts
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
from rest_framework.views import APIView
from .models import User, Recipe  # Import your custom MongoEngine User model
from mongoengine.errors import NotUniqueError
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserDietSerializer
from .serializers import UserSerializer, AddFavoriteRecipeSerializer
from mongoengine.errors import ValidationError as MongoValidationError
from bson.objectid import ObjectId, InvalidId
from .serializers import RecipeSerializer
from .serializers import RemoveFavoriteRecipeSerializer


# API view for user registration
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # Prepare response data without the password
        response_data = {
            "username": user.username,
            "email": user.email,
            # Include other fields if necessary
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API view for user login
@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'detail': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Find the user by email
        user = User.objects.get(email=email)
        # Check the password
        if check_password(password, user.password):
            # Authentication successful; return user info
            return Response({
                'userId': str(user.id),  # Include userId in the response
                'username': user.username,
                'email': user.email,
                # Include other fields if necessary
            }, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

# Serializer for updating user preferences
class UpdatePreferencesSerializer(serializers.Serializer):
    userId = serializers.CharField(required=True)  # Add userId as a required field
    religious_restrictions = serializers.ChoiceField(
        choices=User.RELIGIOUS_RESTRICTIONS_OPTIONS,
        required=False
    )
    diet = serializers.ChoiceField(
        choices=User.DIET_OPTIONS,
        required=False
    )
    allergies = serializers.ListField(
        child=serializers.ChoiceField(choices=User.ALLERGY_OPTIONS),
        required=False
    )

    def validate_allergies(self, value):
        if 'None' in value and len(value) > 1:
            raise serializers.ValidationError("'None' cannot be selected with other allergies.")
        return value

# API view for updating user preferences
class UpdatePreferencesView(APIView):
    # Remove the IsAuthenticated permission class
    # permission_classes = [IsAuthenticated]

    def put(self, request):
        """
        PUT /users/preferences/ to update user preferences.
        Expects 'userId' in the request body to identify the user.
        """
        serializer = UpdatePreferencesSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data.get('userId')

            try:
                # Fetch the user by userId
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

            # Update user preferences
            data = serializer.validated_data
            if 'religious_restrictions' in data:
                user.religious_restrictions = data['religious_restrictions']
            if 'diet' in data:
                user.diet = data['diet']
            if 'allergies' in data:
                user.allergies = data['allergies']
            user.save()
            return Response({"message": "Preferences updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # View to get the user's diet information
@api_view(['GET'])
def get_user_diet(request):
    if request.method == 'GET':
        #user = request.user
        user = User.objects.first() #for testing
        serializer = UserDietSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # View to update the user's diet information
@api_view(['PUT'])
def update_user_diet(request):
    user_id = request.data.get('userId')  # Get the user ID from the request data
    new_diet = request.data.get('diet')  # Get the new diet from the request data

    # Check if user_id and diet are provided
    if not user_id or not new_diet:
        return Response({'detail': 'User ID and diet are required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Find the user by user_id
        user = User.objects.get(id=user_id)

        # Update the diet
        user.diet = new_diet  # Assuming `diet` is a field in your User model
        user.save()  # Save the changes to the database

        return Response({'detail': 'Diet updated successfully', 'diet': user.diet}, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    except MongoValidationError:
        return Response({'detail': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
    

# serializers.py

class UserPreferencesSerializer(serializers.Serializer):
    userId = serializers.CharField(source='id', read_only=True)
    religious_restrictions = serializers.CharField()
    diet = serializers.CharField()
    allergies = serializers.ListField(child=serializers.CharField())

    def to_representation(self, instance):
        return {
            'userId': str(instance.id),
            'religious_restrictions': instance.religious_restrictions,
            'diet': instance.diet,
            'allergies': instance.allergies,
        }


class GetUserPreferencesView(APIView):
    """
    GET /users/preferences/<user_id>/ to retrieve user preferences by user ID.
    """
    # Uncomment the following lines to require authentication
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    
    def get(self, request, user_id):
        try:
            # Validate and convert user_id to ObjectId
            ObjectId(user_id)  # Raises InvalidId if not a valid ObjectId
        except InvalidId:
            return Response({'detail': 'Invalid user ID.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Retrieve the user by user_id
            user = User.objects.get(id=user_id)
            serializer = UserPreferencesSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Optionally log the exception
            return Response({'detail': 'An error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class AddFavoriteRecipeView(APIView):
    """
    POST /users/add_favorite_recipe/ to add a recipe to the user's favorite_recipes.
    Expects 'user_id' and 'recipe_id' in the request data.
    """
    
    def post(self, request):
        serializer = AddFavoriteRecipeSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            recipe_id = serializer.validated_data['recipe_id']
            
            user = User.objects(id=user_id).first()
            recipe = Recipe.objects(id=recipe_id).first()
            
            if recipe in user.favorite_recipes:
                return Response({'detail': 'Recipe already in favorites.'}, status=status.HTTP_400_BAD_REQUEST)
            
            user.favorite_recipes.append(recipe)
            user.save()
            
            return Response({'message': 'Recipe added to favorites successfully.'}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RemoveFavoriteRecipeView(APIView):
    """
    POST /users/remove_favorite_recipe/ to remove a recipe from the user's favorite_recipes.
    Expects 'user_id' and 'recipe_id' in the request data.
    """
    
    def post(self, request):
        serializer = RemoveFavoriteRecipeSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            recipe_id = serializer.validated_data['recipe_id']
            
            user = User.objects(id=user_id).first()
            recipe = Recipe.objects(id=recipe_id).first()
            
            if not user or not recipe:
                return Response({'detail': 'User or Recipe not found.'}, status=status.HTTP_404_NOT_FOUND)
            
            if recipe not in user.favorite_recipes:
                return Response({'detail': 'Recipe not in favorites.'}, status=status.HTTP_400_BAD_REQUEST)
            
            user.favorite_recipes.remove(recipe)
            user.save()
            
            return Response({'message': 'Recipe removed from favorites successfully.'}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class UserFavoriteRecipesView(APIView):
    """
    GET /users/favorite_recipes/<user_id>/ to retrieve a user's favorite recipes.
    """
    
    def get(self, request, user_id):
        # Validate the user_id format
        if not ObjectId.is_valid(user_id):
            return Response({'detail': 'Invalid user ID.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Retrieve the user
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize the favorite recipes
        serializer = RecipeSerializer(user.favorite_recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
