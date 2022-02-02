from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import  User




class Passwords(models.Model):
    user = models.ForeignKey(User, max_length=150, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    websitenames = models.CharField(max_length=200, null=True, blank=True, unique=True)
    websitepasswords = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user


