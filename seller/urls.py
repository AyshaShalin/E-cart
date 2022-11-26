from django.urls import path
from . import views


app_name = "seller"
urlpatterns=[ 
    
    path('add product',views.add_products_categories,name='add_product'),
    path('home',views.s_home,name='seller_home'),
    path('orders',views.orders,name='orders'),
    path('change password',views.change_password,name='change_password'),   
    path('profile',views.profile,name='profile'),
    path('stock_update',views.stock_update,name='stock_update'),
    path('logout',views.logout,name='logout'),
    path('product_catalogue',views.product_catalogue,name="product_catalogue"),
    path('edit_info',views.edit_info,name='edit_info'),
    
   
    
]