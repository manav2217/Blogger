from django import forms
from django.db.models import fields
from django.forms import widgets
from django.http.response import FileResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm ,PasswordChangeForm
from django.contrib.auth.models import User
from django.views import generic
from froala_editor.fields import FroalaEditor


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        
class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']
        
class UpdateUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['email' , 'first_name' , 'last_name' ]
        
class AddBlogForm(forms.ModelForm):
    Blog.content = forms.CharField(widget=FroalaEditor)
        
    class Meta:
        model = Blog
        fields = ['title' , 'content'  , 'catagory' , 'image']
        
    
        
class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['sub_email']
        labels = {'sub_email':'Enter Email :'}
      
      
class ChangeUserPassword(PasswordChangeForm):
    class Meta:
        model = User
        fields = '__all__'  


        

        