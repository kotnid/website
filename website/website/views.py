from django.shortcuts import render 
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    
    return render(request , 'index.html')

def about(request):
    
    return render(request , 'about.html')

def contact(request):
    
    return render(request , 'contact.html')

class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'accounts/profile.html'
