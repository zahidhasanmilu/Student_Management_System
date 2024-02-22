from django.shortcuts import render, HttpResponseRedirect,get_object_or_404, redirect, HttpResponse
from django.urls import reverse, reverse_lazy

# VIEW
from django.views.generic import CreateView, ListView, DetailView, UpdateView, View, TemplateView, DeleteView

#Authentication
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

#forms
from django.contrib.auth.forms import AuthenticationForm

#models
# from django.contrib.auth.models import User

#EmailBackEnd
from app.EmailBackEnd import EmailBackEnd

#message
from django.contrib import messages

import uuid
#For Multiple fields Filter
from django.db.models import Q

#create View Here  
def BASE(request):
    return render(request, 'base.html')


def LOGIN(request):
    
    return render(request, 'login.html')

def doLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = EmailBackEnd.authenticate(request, username=email, password=password)
        
        if user:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return HttpResponse("This Is Head Of Department Panel")
            elif user_type == '2':
                return HttpResponse("This Is Staff Panel")
            elif user_type == '3':
                return HttpResponse("This Is Student Panel")
            else:
                messages.error(request, 'Email and password are invalid !')
                return redirect('login')
        else:
            messages.error(request, 'Email and password are invalid !')
            return redirect('login')