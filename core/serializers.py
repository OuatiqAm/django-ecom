from rest_framework import serializers

from core.models import Item, Category, OrderItems, Customer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'sku', 'description', 'quantity', 'price', 'get_image', 'get_thumbnail']


class CategoryItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        models = OrderItems
        fields = ['item', 'order', 'quantity']


class CartItemsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        customer = Customer.objects.get(user = user)

        token['user_id'] = customer.customer_id

        return token
