from re import S
from django.shortcuts import render
from rest_framework import serializers

from rest_framework.decorators import api_view
from LostFound.serializers import UserRegSerializer ,LostItemSerializer , FoundItemSerializer
from django.http import HttpRequest, JsonResponse
from .models import Lost_Item, UserRegistration,Found_Item
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication ,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class UserRegAPI(APIView):
    def get(self, request):
        user = UserRegistration.objects.all()
        serializers =UserRegSerializer(user, many=True)
        return Response(serializers.data)
    def post(self,request):
        serializers = UserRegSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


class LostItemAPI(APIView):
    def get(self, request):
        lost_item  = Lost_Item.objects.all()
        serializers =LostItemSerializer(lost_item, many=True)
        return Response(serializers.data)
    def post(self,request):
        serializers = LostItemSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class LostItemDetailAPI(APIView):
    def get_objects(self,id):
        try:
            return Lost_Item.objects.get(id= id )
        except Lost_Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        item = self.get_objects(id=id)
        serializers = LostItemSerializer(item)
        return Response(serializers.data)

    def put(self,request,id):
        item= self.get_objects(id=id)
        serializers=LostItemSerializer(item, data= request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,id):
        item= self.get_objects(id=id)
        item.delete()
        return Response(status = status.HTTP_404_NOT_FOUND)


class FoundItemAPI(APIView):
    def get(self, request):
        lost_item  = Found_Item.objects.all()
        serializers =FoundItemSerializer(lost_item, many=True)
        return Response(serializers.data)
    def post(self,request):
        serializers = FoundItemSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class FoundItemDetailAPI(APIView):
    def get_objects(self,id):
        try:
            return Found_Item.objects.get(id= id )
        except Found_Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        item = self.get_objects(id=id)
        serializers = FoundItemSerializer(item)
        return Response(serializers.data)

    def put(self,request,id):
        item= self.get_objects(id=id)
        serializers=FoundItemSerializer(item, data= request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,id):
        item= self.get_objects(id=id)
        item.delete()
        return Response(status = status.HTTP_404_NOT_FOUND)







'''''
@api_view(['GET','POST'])
def user_registration(request): 
    if request.method == 'GET':
        user = UserRegistration.objects.all()
        serializers =UserRegSerializer(user, many=True)
        return Response(serializers.data)

    elif request.method =='POST':
        serializers = UserRegSerializer(data = request.data)
        if serializers.is_valid():
            return Response(serializers.data,status=status.HTTP_202_ACCEPTED)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','POST','DELETE']):
def
'''