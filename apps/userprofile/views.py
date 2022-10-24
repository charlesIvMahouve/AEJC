from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messagese
from django.db import models
from django.contrib.auth.models import User

from .models import Userprofile

# Create your views here.
