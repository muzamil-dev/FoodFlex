from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

class AddItemView(APIView):
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteItemView(APIView):
    def delete(self, request, item_id):
        try:
            # Validate if `item_id` is a valid ObjectId
            if not ObjectId.is_valid(item_id):
                return Response({"detail": "Invalid item ID."}, status=status.HTTP_400_BAD_REQUEST)

            # Find the item by ID
            item = Item.objects(id=item_id).first()

            if not item:
                return Response({"detail": "Item not found."}, status=status.HTTP_404_NOT_FOUND)
            
            # Delete the item
            item.delete()
            return Response({"detail": "Item deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
