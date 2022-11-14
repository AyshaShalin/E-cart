from itertools import product
from django.shortcuts import render,redirect
import customer
from customer.decorator import auth_customer
from customer.models import Cart
from common.models import Customer
from seller.models import Product

@ auth_customer
def cart(request):
    return render (request,'customer/cart.html') 

def customize(request):
    return render (request,'customer/customization.html')

def filter(request):
    return render (request,'customer/filter.html')

def my_account(request):
    return render (request,'customer/my_account.html')

def product_search(request):
    return render (request,'customer/product_search.html') 
    
def wishlist(request):
    return render (request,'customer/wishlist.html') 

@ auth_customer
def home1(request):
    product = Product.objects.all()
    customer = Customer.objects.get(id = request.session ['customerid'])
    return render(request,'customer/home1.html' ,{'userdata':customer,'products':product})     

def home(request):
    product = Product.objects.all()
    customer = Customer.objects.get(id = request.session ['customerid'])
    return render(request,'customer/home.html' ,{'userdata':customer,'products':product})     


def verify(request):
    return render (request,'customer/otp-verify.html')  

def personal_info (request):
     customer = Customer.objects.get(id = request.session ['customerid'])
     return render (request,'customer/personal_info.html',{"customer" : customer})   

def address (request):
     return render (request,'customer/address.html')                                    

def show (request,p_id):
     product = Product.objects.get(id=p_id) 
     return render (request,'customer/show_product.html',{'product':product})    

def logout (request) :
    del request.session ['customerid']
    request.session.flush()
    return redirect ('common:commonhome')   

def add_to_cart (request,p_id):
    cart = Cart(product_id = p_id,customer_id = request.session['customerid'])
    data_exist = Cart.objects.filter(product_id =p_id , customer_id = request.session ['customerid']).exists()
    if data_exist :
        return redirect ('customer:home') 

def cart (request) :
    customer = Customer.objects.get (id = request.session ['customerid'])
    carts = Cart.objects.all()
    return render (request,'customer/cart.html',{'customer':customer , 'carts' :carts})     

# def view_from_cart (request,cart_id) :
#     carts = Cart.objects.get(id=cart_id)
#     return render (request,'customer/view_from_cart.html',{"carts":carts})      

def change_password (request):
    msg = ''
    if request.method  == 'POST' :
        old_pwd = request.POST ["old_password"]
        new_pwd = request.POST ["new_password"]
        customerid = request.session ['customerid']
        customer = Customer.objects.get(id = customerid)
        if (customer.c_password == old_pwd):
            customer.c_password = new_pwd
            customer.save()

        else :
            msg = "Enter a valid password" 
            return render (request,'customer/change_password.html',{"msg":msg})       

    return render (request,'customer/change_password.html')