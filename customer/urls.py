from django.urls import path
from . import views


app_name = 'customer'
urlpatterns=[ 
    path('cart',views.cart,name='cart'),
    path('customize products',views.customize,name='customise'),
    path('filter',views.filter,name='filter'),
    path('my account',views.my_account,name='my_account'),
    path('search products',views.product_search,name='search'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('home',views.home,name='home'),
    path('verify',views.verify,name='verify'),
    path('personal-information',views.personal_info,name='personal_info'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('view product/<int:p_id>',views.show,name='view_product'),
    path('logout',views.logout,name='logout'),
    path('add_to_cart/<int:p_id>',views.add_to_cart,name='add_to_cart'),
    path('cart',views.cart,name='cart'),
    path('change_password',views.change_password,name='change_password'),
    path('remove_cart/<int:p_id>',views.remove_cart,name="remove_cart"),
    path('category/<int:c_id>',views.get_category,name="category"),
    path('total_amount',views.total_amount,name="total_amount"),

    
]