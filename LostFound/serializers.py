from rest_framework import serializers
from rest_framework.response import Response
from .models import UserRegistration,Lost_Item,Found_Item




class UserRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields =['id','first_name','last_name','user_name','user_email','password']
    
    
          


class LostItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lost_Item
        fields =['id','item_name','location','description','image','user','contact']



class FoundItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Found_Item
        fields =['id','item_name','location','description','image','user','contact']
