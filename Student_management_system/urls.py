"""
Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

# views
from .import views, Hod_views, Staff_views, Student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE.as_view(), name='home'),


    path('', views.LOGIN.as_view(), name='login'),
    path('doLogin/', views.doLogin.as_view(), name='doLogin'),
    path('doLogout/', views.doLogout, name='logout'),
    
    #Profile Update
    path('profile/', views.PROFILE.as_view(), name='profile'),


#Hod Panel
    path('Hod/Home/', Hod_views.HOME.as_view(), name='hod_home'),
    path('Hod/Student/Add/', Hod_views.ADD_STUDENT.as_view(), name='add_student'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
