from django import forms
from app.models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class ProfilePicForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ("profile_pic",)

