from django.urls import path
from . import views


app_name = "ecom_admin"

urlpatterns = [ 
  path ('home' ,views.home,name="home"),
  path('add_categories',views.add_categories,name="add_categories"),
  path('approve_seller',views.approve_seller,name="approve_seller"),
  path('view_seller',views.view_seller,name="view_seller"),
  path('view_user',views.view_user,name="view_user"),
  path('load_seller',views.load_seller,name="load_seller"),
  path('delete_seller',views.delete_seller,name="delete_seller"),
  path('seller_approval',views.seller_approval,name="seller_approval"),
  path('approved_Sellers',views.approved_Sellers,name="approved_Sellers"),
  path('users',views.users_show,name="users_show")
]