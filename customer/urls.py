from django.urls import path
from . import views


urlpatterns=[ 
    path('login',views.login),
    path('cart',views.cart),
    path('customize products',views.customize),
    path('filter',views.filter),
    path('order',views.order),
    path('search products',views.product_search),
    path('sign up',views.signup),
    path('wishlist',views.wishlist)

]