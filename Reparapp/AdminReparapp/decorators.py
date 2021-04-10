from django.http import HttpResponse
from django.shortcuts import redirect

def unauthentic_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request,*args, **kwargs)
    return wrapper_func


def allowed_agente():
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_agente:
                return view_func(request,*args, **kwargs)
            else:
                return HttpResponse('No está autorizado')
        return wrapper_func
    return decorator