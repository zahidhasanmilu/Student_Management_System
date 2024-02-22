from django.shortcuts import render, HttpResponseRedirect,get_object_or_404, redirect
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