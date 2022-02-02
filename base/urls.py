from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign_up/', views.signup, name="signup"),
    path('sign_in/', views.sign_in, name='signin'),
    path('myprofile/<str:pk>/', views.profile_page, name="profilepage"),
    path('sign_out/',  views.user_sign_out, name='signout'),
    path('addpass/', views.add_password, name='addpassword'),
    path('viewpass/<str:id>/<str:pwd>/', views.view_pass, name='viewpass'),
    path('deletepass/<str:pwd>', views.delete_pass, name='deletepass'),
    path('editpass/<str:id>/<str:pwd>/', views.edit_pass, name='editpass')
    
]
