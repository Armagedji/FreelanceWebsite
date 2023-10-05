from django.urls import path
from . import views

urlpatterns = [
    path("loginUser", views.loginUser, name="loginUser"),
    path("logoutUser", views.logoutUser, name='logoutUser'),
    path("registerUser", views.registerUser, name='registerUser')
]