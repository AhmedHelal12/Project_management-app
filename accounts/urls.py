
from django.urls import path, include
from django.contrib.auth.views import LoginView,LogoutView
from accounts.forms import UserLoginForm,UserCreationForm
from accounts.views import RegisterView,UserprofileView

urlpatterns = [
    path('login/',LoginView.as_view(authentication_form=UserLoginForm),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('profile/',UserprofileView.as_view(),name='profile'),
    path('',include('django.contrib.auth.urls'))
]
