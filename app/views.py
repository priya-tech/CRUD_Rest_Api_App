from django.shortcuts import render
from rest_framework.views import APIView
from .models import UserModel
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class UserList(APIView):
    def get(self, request, format=None):
        data = UserModel.objects.all()
        serializer = UserSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        print("valid", serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class UserDetails(APIView):
    def get(self, request, pk):
        try:
            user_data = UserModel.objects.get(pk=pk)
            serializer = UserSerializer(user_data)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        user_data = UserModel.objects.get(pk=pk)
        serializer = UserSerializer(user_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        UserModel.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
