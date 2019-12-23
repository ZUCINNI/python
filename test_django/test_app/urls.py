from django.urls import path
from django.contrib.auth import views as viewAuth
from . import views
# from .views import MyRegisterFormView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    path('', viewAuth.LoginView.as_view(), name='login'),
    path('logout/', viewAuth.LogoutView.as_view(), name='logout'),
    path('welcome/', views.welcome, name='welcome'),
    path('register/', views.register, name="register"),
]