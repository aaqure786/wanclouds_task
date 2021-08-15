from django.shortcuts import render
from rest_framework import serializers

from rest_framework.decorators import api_view
from .serializers import UserRegSerializer
from django.http import HttpRequest, JsonResponse
from .models import UserRegistration
from rest_framework.response import Response
from rest_framework import status


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
