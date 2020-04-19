from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SectionSerializer, DestituteSerializer,CardsSerializer,UsersSerializer,CompanySerializer
from .models import Section, Destitute,Cards,Users,Company
from rest_framework.permissions import IsAdminUser, AllowAny, SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly,IsAdminUser

# Create your views here.

class signUp(CreateAPIView):
    model = User
    serializer_class = UserSerializer

class Logout(APIView):
      def get(self, request):
        logout(request)
        data = {'success': 'Sucessfully logged out'}
        return Response(data=data, status=status.HTTP_200_OK)


class SectionViews(APIView):
    serializer_class = SectionSerializer
    permission_classes = (IsAdminUser,)
    def get(self, request, format=None):
        sections = Section.objects.all()
        serializer = self.serializer_class(sections, many=True)
        return Response(serializer.data)
   
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
             sections = Section(name = serializer.validated_data.get("name"))
             sections.save()
             response_serializer = self.serializer_class(sections)
             return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, format=None):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            sections = Section.objects.get(pk=request.POST["name"])
            sections.save()
            response_serializer = self.serializer_class(sections)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DeleteSectionView(APIView):

    def delete(self, request, pk, format=None):
        Section.objects.get(pk=pk).delete()
        return Response({"success": "1 section deleted"}, status=200)


class DestituteViews(APIView):
    serializer_class = DestituteSerializer
    permission_classes = (IsAdminUser,)
    def get(self, request, format=None):
        destitute = Destitute.objects.all()
        serializer = self.serializer_class(destitute, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            destitute = Destitute(
             name = serializer.validated_data.get("name"),
             description = serializer.validated_data.get("description"), 
             iin = serializer.validated_data.get("iin"), 
             phone = serializer.validated_data.get("phone"),  
             cardNumber = serializer.validated_data.get("cardNumber"), 
             address = serializer.validated_data.get("address"), 
             section = Section.objects.get(pk=request.POST["section"]),
             image = request.data.get("image"))
            destitute.save()
            response_serializer = self.serializer_class(destitute)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, format=None):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            destitute = Destitute.objects.get(pk=request.POST["id"])
            destitute.name = serializer.validated_data.get("name")
            destitute.description = serializer.validated_data.get("description")
            destitute.iin = serializer.validated_data.get("iin")
            destitute.phone = serializer.validated_data.get("phone")
            destitute.section = Section.objects.get(pk=request.POST["section"])
            destitute.cardNumber = serializer.validated_data.get("cardNumber")
            destitute.address = serializer.validated_data.get("address")
            destitute.save()
            response_serializer = self.serializer_class(destitute)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DeleteDestituteView(APIView):

    def delete(self, request, pk, format=None):
        Destitute.objects.get(pk=pk).delete()
        return Response({"success": "1 destitute deleted"}, status=200)


class CardsViews(APIView):
    serializer_class = CardsSerializer
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        cards = Cards.objects.filter(author = request.user)
        serializer = self.serializer_class(cards, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            cards = Cards(
             cardNumber = serializer.validated_data.get("cardNumber"),
             cvv = serializer.validated_data.get("cvv"), 
             balance = serializer.validated_data.get("balance"), 
             validDate = serializer.validated_data.get("validDate"),  
             author = request.user)
            cards.save()
            response_serializer = self.serializer_class(cards)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, format=None):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            cards = Cards.objects.get(pk=request.POST["id"])
            cardNumber = serializer.validated_data.get("cardNumber"),
            cvv = serializer.validated_data.get("cvv"),  
            validDate = serializer.validated_data.get("validDate"), 
            cards.save()
            response_serializer = self.serializer_class(cards)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DeleteCardView(APIView):

    def delete(self, request, pk, format=None):
        Cards.objects.get(pk=pk).delete()
        return Response({"success": "1 destitute deleted"}, status=200)

class ProfileViews(APIView):
    serializer_class = UsersSerializer
    permission_classes = (IsAuthenticated,)
    def get(self, request,format=None):
        profile = Users.objects.filter(users = request.user)
        serializer = self.serializer_class(profile, many=True)
        return Response(serializer.data)
   
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
             profile = Users(
                 name = serializer.validated_data.get("name"),
                 phone = serializer.validated_data.get("phone"),
                 cardBalance = serializer.validated_data.get("cardBalance"),
                 address = serializer.validated_data.get("address"),
                 users = request.user)
             profile.save()
             response_serializer = self.serializer_class(profile)
             return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, format=None):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            profile = request.user
            profile.name = serializer.validated_data.get("name"),
            profile.phone = serializer.validated_data.get("phone"),
            profile.cardBalance = serializer.validated_data.get("cardBalance"),
            profile.address = serializer.validated_data.get("address"),
            profile.save()
            response_serializer = self.serializer_class(profile)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
