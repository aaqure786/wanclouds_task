from rest_framework import serializers
from .models import UserRegistration,Lost_Item,Found_Item



class UserRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields =['id','firts_name','last_name','user_name','user_email','password']
          
