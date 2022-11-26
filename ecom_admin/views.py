from django.shortcuts import render
from ecom_admin.models import Category
from common.models import Seller
from django.http import JsonResponse
from django.core.mail import send_mail
from common.models import Customer
 

# Create your views here.
def home (request) :
    return render (request,'ecom_admin/home.html')

def add_categories (request):
    msg = ""
    if request.method == 'POST' :
        category_name = request.POST["name"]
        category = Category( name = category_name)
        category.save()
        msg =  "Category added succesfully"
    return render (request,'ecom_admin/add_categories.html' ,{"msg" : msg})  

def approve_seller (request) :
    return render (request,'ecom_admin/approve_seller.html')    

def view_seller (request) :
    return render (request,'ecom_admin/view_seller.html')    
    
def view_user (request) :
    return render (request,'ecom_admin/view_user.html')  


def load_seller(request) :
    seller = Seller.objects.filter (seller_status = 'pending')  
    data = [{'id': seller.id, 'name': seller.s_firstname, 'email': seller.s_email,
             'address': seller.s_address, 'phone': seller.s_number,'image': seller.s_image.url} for seller in seller]
    print(data)
    return JsonResponse({'data': data})  

def delete_seller(request):
    id = request.POST['id']
    seller = Seller.objects.get(id=id)
    seller.delete()
    return JsonResponse({'status': 'seller deleted'})

def seller_approval(request):
    id = request.POST['id']
    seller = Seller.objects.get(id=id)
    seller.seller_status='approved'
    seller.save()
    send_mail(
    'Approved',
    'Hi {{seller.s_firstname}} we are pleased to inform you that user request has been approved.',
    'shalinayesha@gmail.com',
    [seller.s_email],
    fail_silently=False,
)
    return JsonResponse({'status': 'seller approved'})


def approved_Sellers(request):
    seller = Seller.objects.filter(seller_status='approved')
    data = [{'id': seller.id, 'name': seller.s_firstname, 'email': seller.s_email,
             'address': seller.s_address, 'phone': seller.s_number,'image': seller.s_image.url} for seller in seller]        
    print(data)
    return JsonResponse({'data': data})


def users_show(request):
    customer = Customer.objects.all()
    data = [{'id': customer.id, 'name': customer.c_firstname, 'email': customer.c_email,
              'phone': customer.c_number , 'address' : customer.c_address} for customer in customer]        
    print(data)
    return JsonResponse({'data': data})
