from django.shortcuts import render

# Create your views here.
def login (request):
    return render (request,'customer/login.html')

def cart(request):
    return render (request,'customer/cart.html') 

def customize(request):
    return render (request,'customer/customization.html')

def filter(request):
    return render (request,'customer/filter.html')

def order(request):
    return render (request,'customer/order.html')

def product_search(request):
    return render (request,'customer/product_search.html') 

def signup (request):
    return render (request,'customer/signup.html') 

def wishlist(request):
    return render (request,'customer/wishlist.html')                         