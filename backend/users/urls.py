from django.urls import path
from . import views

urlpatterns = [
    path("loginUser", views.loginUser, name="loginUser"),
]