from django.urls import path
from . import views

urlpatterns=[ 
    path('seller-login',views.login)
]