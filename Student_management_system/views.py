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

# models
# from django.contrib.auth.models import User

# Login MIXIN
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from .mixins import LogoutRequiredMixin

# EmailBackEnd
from app.EmailBackEnd import EmailBackEnd

# message
from django.contrib import messages

import uuid
# For Multiple fields Filter
from django.db.models import Q

# create View Here


@method_decorator(never_cache, name='dispatch')
class BASE(LoginRequiredMixin, TemplateView):
    template_name = 'base.html'


@method_decorator(never_cache, name='dispatch')
class LOGIN(LogoutRequiredMixin, View):
    def get(self,  *args, **kwargs):
        return render(self.request, 'login.html')


@method_decorator(never_cache, name='dispatch')
class doLogin(LogoutRequiredMixin, View):
    def post(self,  *args, **kwargs):
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        user = EmailBackEnd.authenticate(
            self.request, username=email, password=password)

        if user:
            login(self.request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return HttpResponse("This Is Staff Panel")
            elif user_type == '3':
                return HttpResponse("This Is Student Panel")
            else:
                messages.error(
                    self.request, 'Email and password are invalid !')
                return redirect('login')
        else:
            messages.error(self.request, 'Email and password are invalid !')
            return redirect('login')


def doLogout(request):
    logout(request)
    messages.success(request, 'Logout Successfully')
    return redirect('login')
