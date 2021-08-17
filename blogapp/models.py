from typing import ClassVar
from django.contrib import auth
from django.contrib.auth.models import User
from django.db import models
from django.db.models.expressions import OrderBy
from django.forms.widgets import MediaDefiningClass
from django.urls import base
from froala_editor.fields import FroalaField
from tinymce.models import HTMLField

from .helper import *




# Create your models here.

class Catagory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


STATUS_CHOICES = (
    (0, 'Draft'),
    (1, 'Publish')
)


class Blog(models.Model):
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = FroalaField()
    image = models.ImageField(upload_to='blogpost' , null=True , blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES ,  default=0)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    @staticmethod
    def get_blog_by_catagory_id(catagory_id):
        if catagory_id:
            return Blog.objects.filter(catagory= catagory_id)
        else:
            return Blog.objects.all()
        
    @staticmethod
    def get_user_blog(user_id):
        if user_id:
            return Blog.objects.filter(author = user_id)

    def save(self, *args, **kwargs):
        self.slug = genslug(self.title)
        super(Blog, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("blog_detail", kwargs={"slug": str(self.slug)})
    
    
    
        
class Comment(models.Model):
    blog = models.ForeignKey(Blog , on_delete=models.CASCADE , related_name="comments")
    user = models.ForeignKey(User , on_delete=models.CASCADE , default=None)
    message = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return 'Comment {} by {}'.format(self.message,self.user)
    
    
class Subscriber(models.Model):
    sub_email = models.EmailField(max_length=256)
