from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Comment out or remove the import of Django's User model to avoid conflicts
# from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
from rest_framework.views import APIView
from .models import User  # Import your custom MongoEngine User model
from mongoengine.errors import NotUniqueError
# Remove JWT-related imports
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.permissions import IsAuthenticated

# Serializer for the MongoEngine User model
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        # Hash the password before saving
        validated_data['password'] = make_password(validated_data['password'])
        try:
            # Create a new user with validated data
            user = User(**validated_data)
            user.save()  # Raises NotUniqueError if email is already used
            return user
        except NotUniqueError:
            raise serializers.ValidationError({"email": "A user with this email already exists."})

    def validate(self, data):
        # Additional custom validation logic can go here
        return data

# API view for user registration
@api_view(['POST'])
def register(request):
    """
    POST /users/register/ to create a new user.
    """
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
    """
    POST /users/login/ to authenticate a user.
    """
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
