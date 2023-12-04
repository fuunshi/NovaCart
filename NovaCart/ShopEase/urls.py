from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("shop", views.shop, name="shop"),
    path("shop/<int:product_id>", views.product, name="product"),
    path("login", views.login, name="login"),
]