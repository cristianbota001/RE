from django.contrib import admin
from django.urls import path,include
from .views import HomePage, LoginPage, RegisterPage, TablePage, LogoutPage

urlpatterns = [
    path('', HomePage, name = "HomePage"),
    path('login/', LoginPage, name = "LoginPage"),
    path("register/", RegisterPage, name = "RegisterPage"),
    path("grades/", TablePage, name = "TablePage"),
    path("logout/", LogoutPage, name = "LogoutPage")
]
