from django.urls import path
from . import views

urlpatterns=[ 
    path('seller-login',views.login),
    path('add products and categories',views.add_products_categories),
    path('coupons',views.coupons),
    path('user details',views.customer_details),
    path('track order',views.track_order),
    
    path('user verification',views.user_verification),
    path('related products',views.related_products),
    

]