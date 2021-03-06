"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from os import name
import django
from django.contrib import admin
from django.contrib.auth.forms import PasswordResetForm
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import re_path
from blogapp.views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', Login.as_view(), name='login'),
    path('', include("blogapp.urls")),
    path('froala_editor/', include('froala_editor.urls')),
    path('tinymce/', include('tinymce.urls')),
    re_path(r'^media(?P<path>.*)$' , serve , {'document_root':settings.MEDIA_ROOT}),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)