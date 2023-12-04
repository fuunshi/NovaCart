from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    return render(request, "ShopEase/home.html", {})

def shop(request):
    return render(request, "ShopEase/products/product_list.html", {
        "products": Product.objects.all()
    })

def product(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, "ShopEase/products/product_detail.html", {
        "product": product,
    })