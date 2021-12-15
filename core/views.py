# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Item, Category, OrderItems
from core.serializers import ItemSerializer, CategoryItemsSerializer, CartItemsSerializer, MyTokenObtainPairSerializer


class ItemsListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = Item.objects.all()
        serializers = ItemSerializer(items, many=True)
        return Response(serializers.data)


class CategoryItemsView(APIView):

    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        items = Item.objects.filter(category=category)
        serializers = ItemSerializer(items, many=True)
        return Response(serializers.data)


class CategoryView(APIView):

    def get(self, request, slug):
        category = Category.objects.filter(slug=slug)
        serializers = CategoryItemsSerializer(category, many=True)
        return Response(serializers.data)


class CategoryListView(APIView):

    def get(self, request):
        category = Category.objects.all()
        serializers = CategoryItemsSerializer(category, many=True)
        return Response(serializers.data)


class OrderItemsView(APIView):

    def post(self, request):
        serializers = CartItemsSerializer(request.data)
        id = serializers.data['id']
        quantity = serializers.data['quantity']

        item = Item.objects.get(id=id)
        if item:
            orderItem = OrderItems(item=item, quantity=quantity)
            orderItem.save()

        return Response()


from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
