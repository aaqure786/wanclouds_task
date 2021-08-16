from re import S
from django.shortcuts import render
from rest_framework import serializers

from rest_framework.decorators import api_view
from LostFound.serializers import UserRegSerializer ,LostItemSerializer , FoundItemSerializer
from .models import Lost_Item, UserRegistration,Found_Item
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Class to Creat User Account
class UserRegAPI(APIView):
    #Function to show the registered users
    def get(self, request):
        user = UserRegistration.objects.all()
        serializers =UserRegSerializer(user, many=True)
        return Response(serializers.data)
        #Function To register new user
    def post(self,request):
        serializers = UserRegSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


# Creating logIn And log out classapi




# Class to Enter Lost Items
class LostItemAPI(APIView):
    # function to get all lost items
    def get(self, request):
        lost_item  = Lost_Item.objects.all()
        serializers =LostItemSerializer(lost_item, many=True)
        return Response(serializers.data)
        #function to Enter new lost items
    def post(self,request):
        serializers = LostItemSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
#class to check the details and update,delete the record which are insideit
class LostItemDetailAPI(APIView):
    # fucntion to check either item id is present or not
    def get_objects(self,id):
        try:
            return Lost_Item.objects.get(id= id )
        except Lost_Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    # function to get the data of given id
    def get(self,request,id):
        item = self.get_objects(id=id)
        serializers = LostItemSerializer(item)
        return Response(serializers.data)
    #function to update the data of given id
    def put(self,request,id):
        item= self.get_objects(id=id)
        serializers=LostItemSerializer(item, data= request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_404_NOT_FOUND)
    #function to delete the item of given id
    def delete(self,request,id):
        item= self.get_objects(id=id)
        item.delete()
        return Response(status = status.HTTP_404_NOT_FOUND)

# Class of found items
class FoundItemAPI(APIView):
    # fucntion to show all the found items 
    def get(self, request):
        lost_item  = Found_Item.objects.all()
        serializers =FoundItemSerializer(lost_item, many=True)
        return Response(serializers.data)
    # function to insert new items in the data base
    def post(self,request):
        serializers = FoundItemSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
# class to check the details fo found items
class FoundItemDetailAPI(APIView):
        # fucntion to check either item id is present or not
    def get_objects(self,id):
        try:
            return Found_Item.objects.get(id= id )
        except Found_Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    # function to show the items agaisnt the given id
    def get(self,request,id):
        item = self.get_objects(id=id)
        serializers = FoundItemSerializer(item)
        return Response(serializers.data)
    # function to update the record against the given id
    def put(self,request,id):
        item= self.get_objects(id=id)
        serializers=FoundItemSerializer(item, data= request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_404_NOT_FOUND)
    # function to delet the record against the id
    def delete(self,request,id):
        item= self.get_objects(id=id)
        item.delete()
        return Response(status = status.HTTP_404_NOT_FOUND)




