"""
URL configuration for App_creation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Receipe_app.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('delete-reciepe/<id>/', delete_receipe, name="delete_reciepe"),
    
    path('update-reciepe/<id>/', update_receipe, name="update_receipe"),
   
    path('receipe/',receipe, name="receipe"),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
urlpatterns+=staticfiles_urlpatterns()

