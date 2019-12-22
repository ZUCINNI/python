from django.urls import path
from django.contrib.auth import views as viewAuth
from . import views
from .views import MyRegisterFormView

urlpatterns = [
    path('login/', viewAuth.LoginView.as_view(), name='login'),
    path('logout/', viewAuth.LogoutView.as_view(), name='logout'),
    path('welcome/', views.welcome, name='welcome'),
    path('register/', MyRegisterFormView.as_view(), name="register"),
]