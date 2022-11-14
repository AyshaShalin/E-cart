from unicodedata import category
from django.shortcuts import render,redirect

from common.models import Seller
from seller.decorator import auth_seller
from seller.models import Product

# Create your views here.

def add_products_categories (request):
    seller = Seller.objects.get(id = request.session ["sellerid"])
    msg =''
    if request.method == 'POST' :
        if 'add_product' in request.POST :
            prod_name = request.POST ["product_name"]
            prod_num  = request.POST ["product_number"]
            prod_details = request.POST ["product_details"]
            prod_price = request.POST ["product_price"]
            prod_stock = request.POST ["product_stock"]
            prod_image = request.FILES ["product_image"]
            product = Product(
                p_name =   prod_name, 
                p_number = prod_num,
                p_details = prod_details,
                p_price =  prod_price,
                p_stock =  prod_stock,
                p_image =  prod_image,
                seller_id = request.session ["sellerid"]
            )
            product.save()
            msg = 'Succesfully added product'
    return render (request,'seller/add_products.html',{"sellerdata":seller , 'message':msg})  

@ auth_seller
def s_home (request):
    seller = Seller.objects.get(id = request.session ["sellerid"])
    return render (request,'seller/seller_home.html',{"sellerdata":seller})

def change_password(request):
    seller = Seller.objects.get(id= request.session['sellerid'])
    msg = ''
    if request.method == 'POST' :
        old_pwd = request.POST ['old_password']
        new_pwd = request.POST ['new_password']
        sellerid = request.session ['sellerid']
        sellers = Seller.objects.get(id = sellerid) 
        if (sellers.s_password == old_pwd) :
            sellers.s_password = new_pwd
            sellers.save()
        else :
            msg = 'Enter a valid password'
            return render (request,'seller/change_password.html',{'msg':msg , "sellerdata":seller})

    return render (request,'seller/change_password.html',{"sellerdata":seller})

@ auth_seller
def orders (request): 
    return render(request,'seller/order.html') 

def profile (request):
    return render (request,'seller/profile.html')

def stock_update (request):
    return render (request,'seller/stock_update.html')

def logout (request) :
    del request.session ['sellerid']
    request.session.flush ()  
    return redirect ('common:commonhome') 

  