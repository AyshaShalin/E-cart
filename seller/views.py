from unicodedata import category
from django.shortcuts import render

# Create your views here.
def login (request):
    return render (request,'seller/login.html')

def add_products_categories (request):
    return render (request,'seller/add_products.html')  

def coupons (request):
    return render (request,'seller/coupons.html')

def customer_details(request):
    return render (request,'seller/customer_details.html')

def track_order (request): 
    return render(request,'seller/order_tracking.html') 

def related_products (request):
    return render (request,'seller/related_products.html')

def user_verification (request):
    return render (request,'seller/user_verification.html')

  