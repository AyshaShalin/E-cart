from django .shortcuts import render,redirect

def auth_customer (func) :
    def wrap (request):
        if 'customerid' in request.session :
            return func(request)
        else :
            return redirect ('common:customer_login')  

    return wrap   