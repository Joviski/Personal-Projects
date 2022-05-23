from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd= form.cleaned_data
            user= authenticate(request,
                               username=cd['username'],
                               password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated Successfully')

                else:
                    return HttpResponse('Disabled account')

            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request,'account/login.html',{'form': form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form= UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password']) #The set_password method is for hashing "Security Level"
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html',{'new_user': new_user})

    else:
        user_form= UserRegistrationForm()
    return render(request, 'account/register.html',{'user_form': user_form})


#Profile
@login_required
def edit(request):
    if request.method =='POST':
        user_form= UserEditForm(instance= request.user, data=request.POST)
        profile_form= ProfileEditForm(instance=request.user.profile, data=request.POST, files= request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm (instance=request.user.profile)

    return render (request, 'account/edit.html', {'user_form':user_form, 'profile_form':profile_form})


@login_required
def user_list(request):
    users= User.objects.filter(is_active=True)
    return render(request,'account/user/list.html',{'section':'people', 'users':users})

@login_required
def user_detail(request,username):
    user= get_object_or_404(User,username=username,is_active=True)
    return render(request,'account/user/detail.html',{'section': 'people', 'user': user})