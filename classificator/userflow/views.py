from django.shortcuts import render, redirect
from .forms import CreateUserForm, UpdateProfileForm, UpdateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, allowed_users


@allowed_users(allowed_roles=['user'])
def update_profile_page(request):
    if request.method == 'POST':
        form1 = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form1.is_valid():
            form1.save()
        form2 = UpdateUserForm(request.POST, instance=request.user)
        if form2.is_valid():
            form2.save()
        return redirect('user')
    form = UpdateProfileForm(instance=request.user.profile)
    form2 = UpdateUserForm(instance=request.user)
    context = {
        'userform': form2,
        'form': form,
    }
    return render(request, 'update_user.html', context=context)

# Create your views here.
@allowed_users(allowed_roles=['user'])
def user_page(request):
    images = request.user.image_set.all()
    context = {
        'images': images,
    }
    return render(request, 'user.html', context)

@unauthenticated_user
def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created for ' + form.cleaned_data.get('username'))
            return redirect('login')
    context = {
        'form': form,

    }
    return render(request, 'register.html', context)

@unauthenticated_user
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect!')
    return render(request, 'registration/login.html')

@allowed_users(allowed_roles=['user'])
def logout_page(request):
    logout(request)
    return redirect('login')