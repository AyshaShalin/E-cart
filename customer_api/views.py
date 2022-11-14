from django.shortcuts import render
from rest_framework.response import Response
from common.models import Customer
from rest_framework.decorators import api_view 
from .serializer import CustomerSerializer
from django.http import JsonResponse
# Create your views here.

@api_view (['GET'])
def load_customer (request) :
    customer = Customer.objects.all()
    seraialized_data = CustomerSerializer (customer,many = True)
    return JsonResponse (seraialized_data.data,safe=False)


@api_view (['POST'])
def add_customer (request):
    serialized_data = CustomerSerializer (data= request.data)
    if serialized_data.is_valid() :
        serialized_data.save()
        return JsonResponse ({"message" : "Customer is added"})
    else :
        return JsonResponse ({"customer is not added"})


@api_view (['PUT'])
def update_customer (request,id) :
    customer = Customer.objects.get(id = id)
    serialized_data = CustomerSerializer (customer,data = request.data)
    if serialized_data.is_valid() :
        serialized_data.save()   
        return JsonResponse ({"message" : "Customer is updated"}) 
    else :
        return JsonResponse ({"message" : "Customer is not updated"}) 
            

@api_view (['DELETE'])
def delete_customer (request,id) :
    customer = Customer.objects.get(id = id)
    customer.delete()
    return JsonResponse ({"message" : "customer is deleted"})