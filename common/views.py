from django.shortcuts import render,redirect
from django.http import JsonResponse
from common.models import Customer, Seller
from customer import views
from . models import Customer
from seller.models import Product


# Create your views here.


def home (request):
    product = Product.objects.all()
    return render (request,'common/home.html',{"products" : product}) 

def c_signup (request) :
    if request.method == 'POST' :
        if 'c_signup' in request.POST :
            customer_firstname = request.POST ["c_firstname"]
            customer_secondname = request.POST ["c_secondname"]
            customer_email = request.POST ["email"]
            customer_number = request.POST ["phone"]
            customer_address = request.POST ["address"]
            customer_password = request.POST ["password"]
            customer = Customer (
                c_firstname  = customer_firstname,
                c_secondname = customer_secondname,
                c_email      =  customer_email,
                c_number     =  customer_number,
                c_address    =  customer_address,
                c_password   =  customer_password
            )
            customer.save()

    return render (request,'common/customer_signup.html')    

def c_login (request) :
    message = ''
    if 'c_login' in request.POST :
        customer_email = request.POST ["email"]
        customer_password = request.POST ["password"]
        data_exist = Customer.objects.filter(c_email  = customer_email,c_password = customer_password).exists()
        if data_exist :
            customer = Customer.objects.get(c_email  = customer_email,c_password = customer_password)
            request.session['customerid'] = customer.id
            return redirect ('customer:home')
        else :
            message = "Enter a valid email and password"
    return render (request,'common/customer_login.html' ,{"message" : message})    


def s_signup (request) :
    if request.method == 'POST' :
        if 's_signup' in request.POST :
            seller_firstname = request.POST ["s_firstname"]
            seller_secondname = request.POST ["s_secondname"]
            seller_email = request.POST ["email"]
            seller_phone = request.POST ["phone"]
            seller_address = request.POST ["address"]
            seller_accnt = request.POST ["account_no"]
            seller_accntholder = request.POST ["account_holder"]
            seller_ifsc = request.POST ["ifsc"]
            seller_image = request.FILES ["image"]
            seller_password = request.POST ["password"]
            seller  = Seller(
                s_firstname     = seller_firstname,
                s_secondname    = seller_secondname,
                s_email         = seller_email,
                s_number        = seller_phone,
                s_address       = seller_address,
                s_accountnumber = seller_accnt,
                s_ifsc          = seller_ifsc,
                s_accholder     = seller_accntholder,
                s_password      = seller_password ,
                s_image         = seller_image
            )
            seller.save()
 

    return render (request,'common/seller_signup.html')

def s_login (request) :
    message= ''
    if 's_login' in request.POST :
        seller_email = request.POST ["email"]
        seller_password = request.POST ["password"]
        data_exist = Seller.objects.filter ( s_email = seller_email, s_password = seller_password).exists()
        if data_exist :
            seller = Seller.objects.get(s_email = seller_email, s_password = seller_password)
            request.session ["sellerid"] = seller.id
            return redirect ('seller:seller_home')
        else :
            message = "Enter a correct email and password"
    return render (request,'common/seller_login.html' ,{"message" : message})    


def c_email_exist (request) :
    c_email = request.POST ["c_email"]
    c_email_exist = Customer.objects.filter(c_email = c_email).exists()
    return JsonResponse ({"status" : c_email_exist})

def s_email_exist (request) :
    s_email = request.POST["s_email"] 
    s_email_exist = Seller.objects.filter(s_email = s_email).exists()
    return JsonResponse ({"status" : s_email_exist})
    