from django.urls import path
from .views import UserRegAPI,LostItemAPI,LostItemDetailAPI,FoundItemAPI,FoundItemDetailAPI, GeneriApiView


urlpatterns = [
    # url to register new users and to see the registerd user


    path('user_registration/',UserRegAPI.as_view(), name="user_registration"),

    path('generic/user_registration/',GeneriApiView.as_view(), name="generic/user_registration/"),

    path('generic/user_registration/<int:id>/',GeneriApiView.as_view(), name="generic/user_registration/<int:id>"),


    # url to show the losst items and to insert new lost item

    path('lost_item/',LostItemAPI.as_view(), name="lost_item"),


    # url to show,update and delete a single lost item


    path('lost_detail/<int:id>/',LostItemDetailAPI.as_view(),name="lost_detail"),


    #url to show found items and to insert new items


    path('found_item/',FoundItemAPI.as_view(), name="found_item"),


    #url to show,delete and update a single found item


    path('found_detail/<int:id>/',FoundItemDetailAPI.as_view(),name="found_detail"),
]
