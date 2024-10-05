from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

@api_view(['POST'])
def chat_with_ai(request):
    user_message = request.data.get('message', '')

    if not user_message:
        return Response({"error": "No message provided"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Use a newer model, like gpt-3.5-turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can also use gpt-4 if available
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        # Extract the assistant's reply
        bot_reply = response['choices'][0]['message']['content'].strip()

        return Response({"reply": bot_reply}, status=status.HTTP_200_OK)

    except Exception as e:
        print(f"Error in OpenAI request: {str(e)}")  # Print the error to the console
        return Response({"error": "Something went wrong", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
