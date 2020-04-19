from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Product,Category, Comments, Rating, Basket, Order,OrderItem
from myauth.models import Foundation, Company, Section, Destitute, Users,Cards
from .serializers import ProductSerializer, CategorySerializer, CommentsSerializer,OrderItemSerializer, RatingSerializer, BasketSerializer,OrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny, SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly,IsAdminUser

class ProductViews(APIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data)

class CreateProductViews(APIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUser,)
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            product = Product(
             title = serializer.validated_data.get("title"),
             price = serializer.validated_data.get("price"), 
             discountprice = serializer.validated_data.get("discountprice"), 
             discountPercent = serializer.validated_data.get("discountPercent"),  
             quantity = serializer.validated_data.get("quantity"), 
             is_active = serializer.validated_data.get("is_active"), 
             link = serializer.validated_data.get("link"),  
             onsale = serializer.validated_data.get("onsale"), 
             category = Category.objects.get(pk=request.POST["category"]),
             author = Company.objects.get(pk=request.POST["username"]),
             image = request.data.get("image"))
            product.save()
            response_serializer = self.serializer_class(product)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, format=None):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data.get("title"))
            print(serializer.validated_data.get("id"))
            product = Product.objects.get(pk=request.POST["id"])
            product.title = serializer.validated_data.get("title")
            product.discountprice = serializer.validated_data.get("discountprice")
            product.discountPercent = serializer.validated_data.get("discountPercent")
            product.onsale = serializer.validated_data.get("onsale")
            product.category=Category.objects.get(pk=request.POST["category"])
            product.quantity = serializer.validated_data.get("quantity")
            product.is_active = serializer.validated_data.get("is_active")
            product.link = serializer.validated_data.get("link") 
            product.save()
            response_serializer = self.serializer_class(product)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DeleteProductView(APIView):

    def delete(self, request, pk, format=None):
        Product.objects.get(pk=pk).delete()
        return Response({"success": "1 product deleted"}, status=200)



class CommentsViews(APIView):
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request, product_id,format=None):
        comments = Comments.objects.select_related('author').filter(product=product_id)
        serializer = self.serializer_class(comments, many=True)
        return Response(serializer.data)
        
class CreateCommentsViews(APIView):
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
             comments = Comments(text = serializer.validated_data.get("text"),
             created_on = serializer.validated_data.get("created_on"), 
             product = Product.objects.get(pk=request.POST["product"]),
             author = request.user)
             comments.save()
             response_serializer = self.serializer_class(comments)
             return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, format=None):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data.get("text"))
            comments = Comments.objects.get(pk=request.POST["id"])
            comments.text = serializer.validated_data.get("text")
            comments.product = Product.objects.get(pk=request.POST["product"])
            comments.save()
            response_serializer = self.serializer_class(comments)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DeleteCommentsView(APIView):

    def delete(self, request, pk, format=None):
        Comments.objects.get(pk=pk).delete()
        return Response({"success": "1 comments deleted"}, status=200)

class CategoriesViews(APIView):
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser,)
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = self.serializer_class(categories, many=True)
        return Response(serializer.data)
   
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
             categories = Category(name = serializer.validated_data.get("name"))
             categories.save()
             response_serializer = self.serializer_class(categories)
             return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, format=None):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            categories = Category.objects.get(pk=request.POST["name"])
            categories.save()
            response_serializer = self.serializer_class(categories)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DeleteCategoryView(APIView):

    def delete(self, request, pk, format=None):
        Category.objects.get(pk=pk).delete()
        return Response({"success": "1 comments deleted"}, status=200)

class GetCategoriesViews(APIView):
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = self.serializer_class(categories, many=True)
        return Response(serializer.data)
   
class GetProductViews(APIView):
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data)

class BasketView(APIView):

    serializers_class = BasketSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, format=None):
        baskets = Basket.objects.select_related('product').filter(author=request.user)
        serializer = self.serializers_class(baskets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializers_class(data=request.data)
        if(serializer.is_valid()):
        
            try:
                basket_item = Basket.objects.get(author=request.user, product=serializer.validated_data.get('product'))
                basket_item.amount = basket_item.amount + serializer.validated_data.get('amount')
                basket_item.save()
                return Response(self.serializers_class(basket_item).data)
            except Basket.DoesNotExist:
                serializer.save(author=request.user, product=Product.objects.get(pk=request.data["product"]))
            
            return Response(serializer.data)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class DeleteBasketView(APIView):

    serializers_class = BasketSerializer
    permission_classes = (IsAuthenticated, )

    def delete(self, request, pk, format=None):
        content = {
            'status': 'Not Found'
        }
        try:
            basket_item = Basket.objects.get(pk=pk)
            basket_item.delete()
            return Response(content, status=200)
        except Basket.DoesNotExist:
            return Response({"message": serializers.errors}, status=status.HTTP_404_NOT_FOUND)


class OrderCreateView(APIView):
    basket_serializers_class = BasketSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, format=None):
        basket = Basket.objects.filter(author=request.user)
        basket_items = self.basket_serializers_class(basket, many=True)
        if len(basket_items.data) > 0:
            order = Order(author=request.user)
            order.save()
           
            for item in basket_items.data:
                order_item = OrderItem(order=order, product=Product.objects.get(pk=item.get('product')), amount=item.get('amount'))
                order_item.save()
            basket.delete()
            return Response({"message": "success"}, status=200)

        return Response({"message": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)

class RatingViews(APIView):
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request, format=None):
        rating = Rating.objects.all()
        serializer = self.serializer_class(rating, many=True)
        return Response(serializer.data)
   
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
             rating = Rating(rate = serializer.validated_data.get("rate"),
             author = request.user,
             product = Product.objects.get(pk=request.POST["product"]))
             rating.save()
             response_serializer = self.serializer_class(rating)
             return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
