from rest_framework import serializers
from django.contrib.auth.models import User
from items.models import Product,Category, Comments, Rating, Basket, Order
from .models import Foundation, Company, Section, Destitute, Users,Cards
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import admin_only,allowed_users

class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ('name')

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = User
        fields = ("id", "username", "password")

class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = ('id', 'username','email','description','phone', 'cardBalance', 'address','author')

class FoundationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Foundation
		fields = ('id', 'name','description','phone', 'cardBalance', 'author')

class CardsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cards
		fields = ('id', 'cardNumber','cvv','balance', 'validDate','author')

class DestituteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Destitute
		fields = ('id', 'name','description','phone', 'cardNumber','iin', 'address','image', 'section')


class SectionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Section
		fields = ('id', 'name')

class UsersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Users
		fields = ('id', 'name','phone', 'cardBalance', 'address')
