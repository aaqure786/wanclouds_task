from django.urls import path
from .views import UserRegAPI,LostItemAPI,LostItemDetailAPI,FoundItemAPI,FoundItemDetailAPI

urlpatterns = [
    path('user_registration/',UserRegAPI.as_view(), name="user_registration"),
    path('lost_item/',LostItemAPI.as_view(), name="lost_item"),
    path('lost_item_detail/<int:id>/',LostItemDetailAPI.as_view(),name="lost_item_detail"),
    path('found_item/',FoundItemAPI.as_view(), name="found_item"),
    path('found_item_detail/<int:id>/',FoundItemDetailAPI.as_view(),name="found_item_detail"),
]
