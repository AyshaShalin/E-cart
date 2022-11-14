# from unicodedata import name
from django.urls import path
# from importlib.resources import path
from .import views
from unicodedata import name

app_name = "common"
urlpatterns = [
    path ('',views.home,name="commonhome"),
    path ('c_signup',views.c_signup,name="customer_signup"),
    path ('c_login',views.c_login,name="customer_login"),
    path ('s_login',views.s_login,name="seller_login"),
    path ('s_signup',views.s_signup,name="seller_signup"),
    path ('c_email_exist',views.c_email_exist,name="c_email_exist"),
    path ('s_email_exist',views.s_email_exist,name="s_email_exist")
]