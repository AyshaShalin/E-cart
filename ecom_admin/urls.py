from django.urls import path
from . import views


app_name = "ecom_admin"

urlpatterns = [ 
  path('home',views.home,name="home")
]