from django.urls import path
from .views import UserRegAPI,LostItemAPI,LostItemDetailAPI

urlpatterns = [
    path('user_registration',UserRegAPI.as_view(), name="user_registration"),
    path('lost_item',LostItemAPI.as_view(), name="lost_item"),
    path('lost_item_detail',LostItemDetailAPI.as_view(),name="lost_item_detail")
]
