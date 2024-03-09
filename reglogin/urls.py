from django.urls import path
from . import views
from .views import UserRegistrationView



urlpatterns = [
   
   
   path('register/', UserRegistrationView.as_view(), name='registration'),
   
   path ('login/',views.UserLoginView.as_view(), name='login'),
   path ('profile/',views.UserAccountUpdateView.as_view(), name='profile'),
   path ('userlogout/',views.user_logout, name='userlogout'),
   path ('passchange/',views.change_password, name='passchange'),
   
   
]