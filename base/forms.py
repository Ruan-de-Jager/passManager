from asyncio.windows_events import NULL
from cProfile import label
from contextlib import nullcontext
from django import forms



class LoginForm(forms.Form):
    username = forms.CharField(label='Username' , max_length=200)
    password = forms.CharField(label='password' , max_length=200)


class AddPasswordForm(forms.Form):
    website_name = forms.CharField(label='Enter the website name',max_length=200)
    website_password = forms.CharField(label='Enter the website password',max_length=200)


class EditPassword(forms.Form):
    website_name = forms.CharField(label='Enter the new password  name',max_length=200)
    website_password = forms.CharField(label='Enter the new  password',max_length=200)