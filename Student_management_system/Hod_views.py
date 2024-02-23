from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect, HttpResponse
from django.urls import reverse, reverse_lazy

# VIEW
from django.views.generic import CreateView, ListView, DetailView, UpdateView, View, TemplateView, DeleteView

# Authentication
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# forms
from django.contrib.auth.forms import AuthenticationForm

# Login MIXIN
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from .mixins import LogoutRequiredMixin

# models
# from django.contrib.auth.models import User

# EmailBackEnd
from app.EmailBackEnd import EmailBackEnd

# message
from django.contrib import messages

import uuid
# For Multiple fields Filter
from django.db.models import Q


@method_decorator(never_cache, name='dispatch')
class HOME(LoginRequiredMixin, TemplateView):
    template_name = 'Hod/home.html'
