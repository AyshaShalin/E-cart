from itertools import product
from django.shortcuts import render,redirect
import customer
from customer.decorator import auth_customer
from customer.models import Cart
from common.models import Customer
from seller.models import Product
from ecom_admin.models import Category
from django .http import JsonResponse

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


# def home1(request):
#     product = Product.objects.all()
#     customer = Customer.objects.get(id = request.session ['customerid'])
#     return render(request,'customer/home1.html' ,{'userdata':customer,'products':product})     
 
@ auth_customer
def home(request):
    product = Product.objects.all()
    customer = Customer.objects.get(id = request.session ['customerid'])
    category = Category.objects.all()
    return render(request,'customer/home.html' ,{'userdata':customer,'products':product ,"categories" :category})     


def verify(request):
    return render (request,'customer/otp-verify.html')  

def personal_info (request):
     customer = Customer.objects.get(id = request.session ['customerid'])
     return render (request,'customer/personal_info.html',{"userdata" : customer})     

def edit_profile (request):
     if request.method == 'POST' :
        first_name = request.POST["first_name"]
        second_name = request.POST ["second_name"]
        address = request.POST ["address"]
        customer = Customer.objects.get (id = request.session['customerid'])
        if (customer.c_firstname == first_name ,
            customer.c_secondname == second_name,
            customer.c_address == address) :
            Customer.objects.filter(id = request.session['customerid']).update(c_firstname = first_name , c_secondname = second_name , c_address = address)                                   
     return render (request,'customer/edit_profile.html',)
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
    cart.save()    
    return redirect ('customer:home')    

def cart (request) :
    customer = Customer.objects.get (id = request.session ['customerid'])
    carts = Cart.objects.all()
    return render (request,'customer/cart.html',{'customer':customer , 'carts' :carts})     

def remove_cart (request ,p_id) :
    cart = Cart.objects.get(product_id = p_id ,customer_id = request.session ['customerid'])
    cart.delete()
    return redirect ('customer:cart')      

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

def get_category (request ,c_id) :
    product = Product.objects.filter ( category_id = c_id)
    return render (request,'customer/category.html' ,{"products" : product})


def total_amount (request) :
    quantity = request.POST ["quantity"]
    price = request.POST ["price"]
    total = int(quantity) * float(price)
    print (total)
    return JsonResponse ({"total" : total})   


