from rest_framework import serializers 
from rest_framework.response import Response
from .models import UserRegistration,Lost_Item,Found_Item
import re




class UserRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields =['id','first_name','last_name','user_name','user_email','password']
    
    def validate_password(sels,value):
        if not re.findall('[0-9]',value):
             raise serializers.ValidationError('password must contain at least one integer')
        elif not re.findall('[a-z]',value):
             raise serializers.ValidationError('password must contain at least one lowercase character')
        elif not re.findall('[A-Z]',value):
             raise serializers.ValidationError('password must contain at least one uppercase character')
        elif not re.findall('[!@#$%^&*\|]',value):
             raise serializers.ValidationError('password must contain at least one symbol')
        return value

    
          


class LostItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lost_Item
        fields =['id','item_name','location','description','image','user','contact']



class FoundItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Found_Item
        fields =['id','item_name','location','description','image','user','contact']
