from django.contrib.messages.api import add_message
from django.db.models.query import EmptyQuerySet
from django.http import request
from django.shortcuts import redirect, render , get_object_or_404 , HttpResponseRedirect
from django.urls.base import reverse
from django.utils.text import re_words 
from .models import *
from django.views import generic
from django.views.generic.edit import CreateView , UpdateView 
from .forms import *
from django.contrib.auth import login , authenticate , logout , update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView , LogoutView ,PasswordChangeView
from django.contrib.auth.decorators import login_required 
from datetime import datetime , timezone
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin 
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
# class PostListView(generic.ListView):
#     model = Blog
#     template_name = "index.html"

def index(request):
    return render(request , "index.html")

@login_required    
def myblogs(request):
    user = request.user
    blogs = None
    if user:
        blogs = Blog.get_user_blog(user)
    return render(request , 'myblogs.html' , {'blogs':blogs})

@login_required
def myprofile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            updateform = UpdateUserForm(request.POST , instance=request.user)
            if updateform.is_valid():
                updateform.save()
                messages.success(request , "Data updated successfully")
        else:
            updateform = UpdateUserForm(instance=request.user)
    userblogs = Blog.get_user_blog(request.user)
    return render(request , 'myprofile.html' , {'userblogs':userblogs , 'updateuser':updateform})
 
@login_required  
def blog_detail(request , slug):
    template_name = "blog-detail.html"
    blog = get_object_or_404(Blog , slug=slug)
    comments = blog.comments.filter()
    new_comment = None
    user = None
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if request.user.is_authenticated:
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.user = User.objects.get(pk=request.user.id)
                new_comment.blog = blog
                new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request , template_name , {
        'blog':blog,
        'new_comment':new_comment,
        'comment_form':comment_form,
        'comments':comments
    })
    
# class PostDetail(generic.DetailView):
#     model = Blog
#     template_name = "blog-detail.html"
         
# def signup(request):
#     if request.method == "GET":
#         form = CreateUser()
#         return render(request , "signup.html" , {'form':form})
#     else: 
#         form = CreateUser(request.POST)
#         if form.is_valid():
#             user = form.save()
#             print(user)
#             if user is not None:
#                 return redirect('index')
#         else:
#             return render(request , "signup.html" , {'form':form})

class SignUp(generic.CreateView):
    form_class = CreateUser
    success_url = reverse_lazy('index')
    template_name = 'signup.html'
    
            
class Login(LoginView):
    template_name = 'login.html'
    
class Logout(LogoutView):
    success_url_allowed_hosts = 'index.html'
   
# class AddBlog(LoginRequiredMixin , CreateView):
#     def form_valid(self, AddBlogForm):
#         new_blog = AddBlogForm.save(commit=False)
#         new_blog.author = self.request.user
#         new_blog.created_on = datetime.today()
#         new_blog.save()
#         messages.success(self.request , f"Your blog is awaiting moderation")
#         return super(AddBlog , self).form_valid(AddBlogForm)
    
#     model = Blog
#     fields = ['title' , 'content' , 'catagory' , 'image']
#     template_name = 'add-blog.html'
#     success_url = reverse_lazy('index')
    
def addblog(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            print(request.POST)
            form = AddBlogForm(request.POST, request.FILES)
            if form.is_valid():
                print(request.POST)
                # blog.image = request.POST.image
                blog = form.save(commit=False)
                blog.author = User.objects.get(pk=request.user.id)
                print(form)
                form.save()
                messages.success(request , "Your blog is awaiting moderation")
                return redirect('index')
            else:
                messages.error(request , form.errors)
                return HttpResponseRedirect('/addblog/')
        else:
            form  = AddBlogForm()
            return render(request , "add-blog.html" , {'form':form})
    else:
        messages.error(request , "Please login to see that page")
        return redirect('login')
    
def deleteblog(request , id):
    Blog.objects.get(id=id).delete()
    return redirect('myblogs')
    
class EditBlogView(LoginRequiredMixin, PermissionRequiredMixin ,generic.UpdateView):
    permission_required = 'blog.change_blog'
    model = Blog
    fields = ['title' , 'catagory' , 'content' , 'image' , 'status']
    success_url = reverse_lazy('index')
    template_name = "editblog.html"

def change_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ChangeUserPassword(request.user , request.POST)
            if form.is_valid():
                user = form.save
                update_session_auth_hash(request , user)
                messages.success(request , "Your password is successfully changed")
                return redirect('index')
            else:
                messages.error(request , form.errors)
                return HttpResponseRedirect('/change_password/')
        else:
            form  = ChangeUserPassword(request.user)
            return render(request , "change-password.html" , {'form':form})
    else:
        messages.error(request , "Please login to see that page")
        return redirect('login')

    




