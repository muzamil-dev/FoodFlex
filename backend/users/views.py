from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User  # Import your custom MongoEngine model
from mongoengine.errors import ValidationError as MongoValidationError
from mongoengine.errors import NotUniqueError
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken


# Serializer for the MongoEngine User model
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

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

        
# API view for user registration
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    """
    POST /users/login/ to authenticate a user and return JWT token.
    """
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        # Find the user by email
        user = User.objects.get(email=email)

        # Check the password
        if check_password(password, user.password):
            # If the password is correct, generate JWT tokens
            refresh = RefreshToken.for_user(user)
            
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'username': user.username,
                'email': user.email,
            }, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    except User.DoesNotExist:
        return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)