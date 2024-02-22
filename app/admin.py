from django.contrib import admin
from app.models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    '''Admin View for CustomUser'''

    list_display = ('username','user_type')
    
