from django.http import HttpResponse
from django.shortcuts import redirect


def admin_only(func):
    def wrapper(request, *args, **kwargs):

        if group == 'admin':
            return func(request, *args, **kwargs)
        else:
            return HttpResponse("You are not admin!")


def allowed_users(allowed_roles=[]):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not allowed to view this page!")
        return wrapper
    return decorator

def unauthenticated_user(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper