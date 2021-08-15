from django.urls import path
from .views import user_registration

urlpatterns = [
    path('user_registration',user_registration, name="user_registration"),
]
