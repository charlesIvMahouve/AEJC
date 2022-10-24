from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your models here.

class Userprofile(models.Model):

    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=20, null=True)