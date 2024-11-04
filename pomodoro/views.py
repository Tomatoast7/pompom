from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class baseview(TemplateView):
    #Template foler already defined in settings.py so you dont have to specify that folder in views
    template_name = 'base.html'

class homeview(TemplateView):
    template_name = 'home.html'