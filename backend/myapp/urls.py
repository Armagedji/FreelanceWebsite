from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="todos"),
    path("todos/upload/", views.upload, name="upload"),
    path("orders/", views.orders, name="orders"),
    path("orders/upload", views.orderUpload, name="orderUpload"),
]
