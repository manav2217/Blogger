from os import name
from django.contrib import admin
from django.contrib.auth.forms import PasswordResetForm
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from blogapp.views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView 

urlpatterns = [
    path('login/', Login.as_view() , name="login"),
    path('', index , name="index"),
    path('signup/', SignUp.as_view() , name="signup" ),  
    path('change_password/' , change_password , name="change_password"),
    
    path('reset_password/' , auth_views.PasswordResetView.as_view(template_name = "forgot-password.html") , name="reset_password"),
    path('reset_password_done/' , auth_views.PasswordResetDoneView.as_view(template_name = "password_reset_done.html") , name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(template_name = "password_reset_confirm.html") , name="password_reset_confirm"),
    path('password_reset_complete/' , auth_views.PasswordResetCompleteView.as_view(template_name = "password_reset_complete.html") , name="password_reset_complete"),
    
    
    
    path('myblogs/', myblogs , name="myblogs" ),
    path('deleteblog/<int:id>/', deleteblog , name="deleteblog" ),
    path('editblog/<slug>/', EditBlogView.as_view() , name="editblog" ),
    path('myprofile/', myprofile , name="myprofile" ),
    path('logout/', Logout.as_view() , name="logout" ),  
    path('addblog/', addblog , name="addblog" ),  
    path('<slug:slug>/', blog_detail , name="blog_detail" ),
    path('froala_editor/', include('froala_editor.urls')),
    path('tinymce/', include('tinymce.urls')),
   
    
]
