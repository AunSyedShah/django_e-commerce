from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from .models import Product

# Create your views here.


def index(request):
    context = {}
    products = Product.objects.all()
    context["products"] = products
    return render(request, "index.html", context)

def sign_in(request):
    return render(request, "sign_in.html")

def sign_up(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password1']
        try:
            User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
        except IntegrityError:
            messages.add_message(request, level=messages.ERROR, message="Username or email already exists")
    return render(request, "sign_up.html")

def forgot_password(request):
    return render(request, "forgot_password.html")
