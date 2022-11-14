from .import views
from django.urls import path

app_name = "customer_api"
urlpatterns = [ 
    path('load_customer',views.load_customer,name="load_customer"),
    path('add_customer',views.add_customer,name="add_customer"),
    path('update_customer/<int:id>',views.update_customer,name="update_customer"),
    path('delete_customer/<int:id>',views.delete_customer,name="delete_customer")
]