from django.contrib import admin
from django.urls import path,include
from .models import business_profile,contact,address,local_support,categories
# Register your models here.

admin.site.register([business_profile,contact,
address,local_support,categories])