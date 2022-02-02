from ast import Pass
from multiprocessing import context
from urllib.request import parse_keqv_list
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, AddPasswordForm, EditPassword
from django.contrib.auth.models import User
from django.contrib import messages
from . models import Passwords
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.hashers import make_password
import os

SECRET_KEY = os.environ['SECRET_KEY']

def home(request):
    user = request.user
    return render(request, 'base/home.html', {'user': user})
    

def signup(request):

    if request.user.is_authenticated:
        return render(request, 'base/profile.html', {})
    else:
        form = UserCreationForm()

        if request.method == "POST":    
                form = UserCreationForm(request.POST)

                if form.is_valid:
                    user = form.save(commit=False)
                    user.username = user.username
                    user.save()


                    login(request, user)
                    return render(request, 'base/profile.html', {})

                    #return render(request, 'base/sign_up.html', {'username':username}, {'id': ''})
                else:
                    messages.error(request,'An error required during the sign up')
        else:
            form = UserCreationForm()
            return render(request, 'base/sign_up.html', {'form':form})

def sign_in(request):

    if request.user.is_authenticated:
        return render(request, 'base/profile.html', {})
    else:
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                db_user = User.objects.get(username=username)
                if db_user == user:

                    return redirect('/myprofile/{0}'.format(request.user.id))
                else:
                    return render(request, 'home', {})
            else:
            #return render(request, 'base/sign_in.html', {'form':form}, {'user':user})
                    return redirect('/')
        else:
            return render(request, 'base/sign_in.html', {'form':form})

@login_required(login_url='sign_in')
def profile_page(request, pk):


    if request.method == 'GET':
        q = request.GET.get('q') if request.GET.get('q') != None else ''
        user = User.objects.get(id=pk)
        passwords = user.passwords_set.filter(
            Q(websitenames__icontains=q)
        )

        

        context = { 'user': user, 
                    'passwords':passwords}
        return render(request, 'base/profile.html', context)
    else:
       
        return render(request, 'base/home.html')


@login_required(login_url='sign_in')
def user_sign_out(request):
    logout(request)
    return redirect('home')

@login_required(login_url="sign_in")
def add_password(request):
    form = AddPasswordForm()
    host = User.objects.get(id=request.user.id)
    

    if request.method == 'POST':
        form = AddPasswordForm(request.POST)
        
        if form.is_valid():
            website_name = request.POST.get('website_name')
            website_password = request.POST.get('website_password')
            primkey = Passwords.objects.count()
            primkey += 1

            Passwords.objects.create(
                user=host,
                id=primkey,
                websitenames=website_name,
                websitepasswords=website_password,
            )

            #return render(request, 'base/addpass.html', {'form':form})
            return redirect("/myprofile/{0}".format(request.user.id))
    return render(request, 'base/addpass.html', {'form':form })


def view_pass(request, id, pwd):

    user = User.objects.get(id=id)
    password = user.passwords_set.get(websitenames=pwd)

    context = {'user':user,'password':password}
    return render(request, 'base/viewpass.html', context)
     
def edit_pass(request, id ,pwd):
    user = User.objects.get(id=id)
    edit_pwd = user.passwords_set.get(websitenames=pwd)
    
    form = EditPassword()

    if request.method == "POST":
        form = EditPassword(request.POST)
        edit_pwd.websitenames = request.POST.get('website_name')
        edit_pwd.websitepasswords = request.POST.get('website_password')
        edit_pwd.save()
        return redirect('/myprofile/{0}'.format(request.user.id))

    context = {'form':form, 'password':pwd}
    return render(request, 'base/editpass.html', context)

def delete_pass(request, pwd):
    user = User.objects.get(id=request.user.id)
    password = user.passwords_set.get(websitenames=pwd)

    if request.method == 'POST':
        password.delete()
        return redirect('/myprofile/{0}'.format(request.user.id))

    return render(request, 'base/deletepass.html', {'password':pwd})
