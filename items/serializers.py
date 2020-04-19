from rest_framework import serializers
from myauth.serializers import UserSerializer
from .models import Product,Category, Comments, Rating, Basket, Order,OrderItem
from myauth.models import Foundation, Company, Section, Destitute, Users,Cards

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('id', 'name')


class CommentsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comments
		fields = ('id', 'text', 'created_on', 'product', 'author')

class ProductSerializer(serializers.ModelSerializer):
	category = CategorySerializer(read_only=True)
	author = UserSerializer(read_only=True)
	class Meta:
		model = Product
		fields = ('id','title', 'price', 'discountprice', 'discountPercent','quantity','is_active','link', 'image','onsale', 'category', 'author')

class RatingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rating
		fields = ('id','rate','product', 'author')


class BasketSerializer(serializers.ModelSerializer):
	class Meta:
		model = Basket
		fields = ('id', 'product', 'author','amount')

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ('id','orderDate', 'author')

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("id", "order", "product", "amount")
