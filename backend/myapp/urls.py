from django.urls import path
from . import views

urlpatterns = [
    path("", views.mainPage, name="mainPageFromGPT"),
    path("todos/", views.todos, name="todos"),
    path("todos/upload/", views.upload, name="upload"),
    path("orders/", views.orders, name="orders"),
    path("orders/upload/", views.orderUpload, name="orderUpload"),
    path("test/", views.test.as_view(), name="test"),
    path("home/", views.home, name="home"),
]
