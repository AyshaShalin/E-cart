from unicodedata import category
from django.shortcuts import render,redirect

from common.models import Seller
from seller.decorator import auth_seller
from seller.models import Product

# Create your views here.
@ auth_seller
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
            category = request.POST["category"]
            product = Product(
                p_name =   prod_name, 
                p_number = prod_num,
                p_details = prod_details,
                p_price =  prod_price,
                p_stock =  prod_stock,
                p_image =  prod_image,
                seller_id = request.session ["sellerid"],
                category_id = category
            )
            product.save()
            msg = 'Succesfully added product'
    return render (request,'seller/add_products.html',{"sellerdata":seller , 'message':msg})  

@ auth_seller
def s_home (request):
    seller = Seller.objects.get(id = request.session ["sellerid"])
    return render (request,'seller/seller_home.html',{"sellerdata":seller})

@ auth_seller
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
            return render (request,'seller/change_password.html',{ 'msg' : msg , "sellerdata" : seller })

    return render (request,'seller/change_password.html',{ "sellerdata" : seller })

@ auth_seller
def orders (request): 
    return render(request,'seller/order.html') 

@ auth_seller
def profile (request):
    seller = Seller.objects.get(id= request.session['sellerid'])
    return render (request,'seller/profile.html' , {"sellerdata" : seller })

@ auth_seller
def stock_update (request):
    return render (request,'seller/stock_update.html')

@ auth_seller
def logout (request) :
    del request.session ['sellerid']
    request.session.flush ()  
    return redirect ('common:commonhome') 

@ auth_seller
def product_catalogue (request) :
    seller = Seller.objects.get(id = request.session ['sellerid'])
    product = Product.objects.filter(seller = request.session ['sellerid'])
    return render (request,'seller/product_catalogue.html' , {"sellerdata" : seller , "products":product})  


def edit_info (request) :
    seller = Seller.objects.get (id = request.session['sellerid'])
    if request.method == 'POST' :
        first_name = request.POST["first_name"]
        second_name = request.POST["second_name"]
        address = request.POST["address"]
        account_no = request.POST["account_number"]
        ifsc = request.POST["ifsc"]
        acc_holder = request.POST["account_holder"]
        # image = request.FILES["product_image"]
        seller = Seller.objects.get(id = request.session['sellerid'])
        if (seller.s_firstname == first_name , seller.s_secondname == second_name , seller.s_address == address ,seller.s_accountnumber == account_no  , seller.s_ifsc == ifsc ,seller.s_accholder == acc_holder) :
            Seller.objects.filter(id = request.session ['sellerid']).update(s_firstname = first_name ,s_secondname = second_name ,s_address = address ,s_accountnumber = account_no , s_ifsc = ifsc ,s_accholder = acc_holder)
    return render (request,'seller/edit_info.html' ,{"sellerdata" : seller})


# def update_profile(request) :
#     if request.method == 'POST' :
#         first_name = request.POST["first_name"]
#         second_name = request.POST["second_name"]
#         address = request.POST["address"]
#         image = request.FILE["product_image"]
#         seller = Seller.objects.get(id = request.session['sellerid'])
#         if (seller.s_firstname == first_name , seller.s_secondname == second_name , seller.s_address == address , seller.s_image == image) :
#             Seller.objects.filter(id = request.session ['sellerid']).update(s_firstname = first_name ,s_secondname = second_name ,s_address = address , s_image = image)
#     return render (request,'seller/update_profile.html' )


