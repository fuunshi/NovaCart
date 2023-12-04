from django.shortcuts import render
from .models import Product
from .forms import LoginForm

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

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
    else:
        form = LoginForm()
        
    return render(request, "ShopEase/user/login.html", {
        'form': form
    })