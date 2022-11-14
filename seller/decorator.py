from msilib.schema import Shortcut
from django.shortcuts import render,redirect
def auth_seller(func) :
    def wrap (request) :
        if 'sellerid' in request.session :
            return func(request)
        else :
            return redirect ('common:seller_login')   

    return wrap         