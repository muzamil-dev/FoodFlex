from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeList(APIView):
    def get(self, request):
        # Fetch all recipes from MongoDB using mongoengine
        recipes = Recipe.objects.all()  # This uses mongoengine's query API
        # Serialize the data to JSON
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
