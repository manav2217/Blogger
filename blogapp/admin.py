from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['author' , 'catagory' , 'title' , 'updated_on' , 'created_on' , 'status']
    list_filter = ['status',]
    search_fields = ['author' , 'title' , 'content']
    prepopulated_fields = {'slug':('title',)}
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user' , 'blog' , 'created_on']
    list_filter = ['created_on']
    search_fields = ['user' ]
    
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['sub_email']

admin.site.register(Blog , BlogAdmin)
admin.site.register(Catagory)
admin.site.register(Comment , CommentAdmin)
admin.site.register(Subscriber , SubscriberAdmin)
