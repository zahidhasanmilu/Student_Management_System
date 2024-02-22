"""
Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

#views
from .import views, Hod_views, Staff_views, Student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BASE, name='home'),
    
    
    path('login/', views.LOGIN, name='login'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)