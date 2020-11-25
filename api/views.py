from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import CreateUserSerializer, UserSerializer,LoginUserSerializer, ProductSerializer, CategorySerializer
from .models import User,  Category, Product
from django.contrib import auth
from rest_framework import status
from django.conf import settings
from .permissions import IsCompanyAdmin, IsNormalUser
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from urllib import request
from django.http  import HttpResponse
from knox.models import AuthToken

from knox.views import LoginView as KnoxLoginView
from rest_framework import viewsets, permissions, generics

import jwt
# Create your views here.



class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class UserView(APIView):
#     permission_classes = (IsAuthenticated,IsCompanyAdmin)
#     def get(self, request):
#         try:
#             users = User.objects.all()
#         except User.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         if request.method == 'GET':
#             serializer = UserSerializer(users, many=True)
#             return Response(serializer.data)


# class HelloView(APIView):
#     permission_classes = (IsAuthenticated,)             # <-- And here

#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)