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

from Student_management_system.forms import ProfilePicForm
from app.models import CustomUser
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



class PROFILE(LoginRequiredMixin,View):
    
    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.get(id = request.user.id)
        
        context={
            'user':user}
        return render(self.request, 'profile.html',context)

    def post(self, request, *args, **kwargs):
        
        # username = request.POST.get('username')
        # email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        profile_pic = request.FILES.get('profile_pic')
        password = request.POST.get('password')
    
        user = CustomUser.objects.get(id = request.user.id)
        user.first_name = first_name
        user.last_name = last_name
        if password !=None and password!="":
            user.set_password(password)
        if profile_pic != None and profile_pic!="":
            user.profile_pic=profile_pic
        user.save()
        return redirect('profile')
    

@login_required
def addProfile_pic(request):
    form = ProfilePicForm(request.FILES)
    if request.method == "POST":
        form = ProfilePicForm(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()  
            messages.success(request, 'Profile Pic Update Succesfully Done')
            return redirect('profile')
    context = {
        'form': form
    }
    return render(request, 'update_profile_pic.html', context)

