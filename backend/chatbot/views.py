from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from bson.objectid import ObjectId
import logging
from users.models import User  # Import your MongoEngine User model
import openai
import os

# Set up logging
logger = logging.getLogger(__name__)

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

@csrf_exempt
@api_view(['POST'])
def chat_with_ai(request):
    try:
        # Get the message and user ID from the request
        message = request.data.get('message')
        user_id = request.data.get('userId')
        logger.info(f'Received message: {message}, from user ID: {user_id}')

        if not message or not user_id:
            return Response({'error': 'Message and userId are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve user details based on user ID, converting the user_id to an ObjectId
        user = User.objects.get(id=ObjectId(user_id))  # Conversion to ObjectId for MongoEngine

        # Fetch user preferences for customization
        user_preferences = {
            "diet": user.diet,
            "religious_restrictions": user.religious_restrictions,
            "allergies": user.allergies,
        }

        # Use the user preferences to customize the prompt for OpenAI
        prompt = f"You are a food assistant that takes into account dietary preferences.\n"
        prompt += f"The user's preferences are:\n"
        prompt += f"Diet: {user_preferences['diet']}\n"
        prompt += f"Religious Restrictions: {user_preferences['religious_restrictions']}\n"
        prompt += f"Allergies: {', '.join(user_preferences['allergies'])}\n\n"
        prompt += f"User Message: {message}\n\nProvide a response that matches the user's dietary preferences."

        # Call OpenAI API to get the response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use gpt-3.5-turbo or another model if available
            messages=[
                {"role": "system", "content": "You are a helpful assistant specializing in dietary advice."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract the assistant's reply
        bot_reply = response['choices'][0]['message']['content'].strip()

        # Return the reply to the user
        return Response({"reply": bot_reply}, status=status.HTTP_200_OK)

    except (User.DoesNotExist, InvalidId) as e:
        logger.error(f'User not found or invalid user ID: {str(e)}')
        return Response({'error': 'User not found or invalid user ID'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        logger.error(f'Unexpected error: {str(e)}')
        return Response({'error': 'An unexpected error occurred.', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
