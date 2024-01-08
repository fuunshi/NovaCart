from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import Product, Message
from django.contrib.auth.models import User
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

def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, "ShopEase/user/login.html", {
                    'form': form,
                    'message': 'Invalid Credentials',
                })
    else:
        form = LoginForm()

    return render(request, "ShopEase/user/login.html", {
        'form': form
    })

def users(request, username):
    return render(request, "ShopEase/user/profile.html", {

    })

def logout_request(request):
    logout(request)
    return render(request, "ShopEase/home.html" , {})

def about(request):
    return render(request, "ShopEase/misc/about.html", {})

def view_messages(request, sender_id, receiver_id):
    sender = User.objects.get(id=sender_id)
    receiver = User.objects.get(id=receiver_id)
    
    messages = Message.objects.filter(sender=sender, receiver=receiver) | Message.objects.filter(sender=receiver, receiver=sender)
    messages = messages.order_by('timestamp')

    context = {
        'messages': messages,
        'receiver': receiver,
        'sender': sender
    }
    return render(request, 'message/message.html', context)