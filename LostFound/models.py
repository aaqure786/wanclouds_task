from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Creating a model 
class UserRegistration(models.Model):
    first_name = models.CharField(max_length=20,null=False, blank=False)
    last_name = models.CharField(max_length=20,blank=False)
    user_name =models.CharField(max_length=20,null=False,blank=False)
    user_email =models.EmailField(max_length=20,null=False,blank=False,unique=True)
    password = models.CharField(max_length=8,null=False,blank=False,unique=True)


    def __str__(self):
        return self.user_name
    @receiver(post_save,sender =settings.AUTH_USER_MODEL)
    def creat_aut_token(sender,instance=None,created = False,**kwarg):
        if created:
            Token.objects.create(user=instance)


class Found_Item(models.Model):
    item_name = models.CharField(max_length=20,null=False)
    location= models.CharField(max_length=20,null=False)
    description =models.CharField(max_length=100,null = True)
    image = models.ImageField(upload_to="images/")
    user = models.ForeignKey(UserRegistration,on_delete=models.CASCADE)
    contact =models.CharField(max_length=15,null=False,blank=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item_name


class Lost_Item(models.Model):
    item_name = models.CharField(max_length=20,null=False)
    location= models.CharField(max_length=20,null=False)
    description =models.CharField(max_length=100,null = True)
    image = models.ImageField(upload_to="images/")
    user = models.ForeignKey(UserRegistration,on_delete=models.CASCADE)
    contact =models.CharField(max_length=15,null=False,blank=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item_name


