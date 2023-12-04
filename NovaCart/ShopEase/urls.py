from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("shop", views.shop, name="shop"),
    path("shop/<int:product_id>", views.product, name="product"),
    path("login", views.login_request, name="login"),
    path('logout', views.logout_request, name='logout'),
    path('about', views.about, name='about'),
    path('<str:username>', views.users, name='user')
]