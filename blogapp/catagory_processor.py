from .models import *

def catagories(request):
    all_catagory = Catagory.objects.all()
    catagory_id = request.GET.get('catagory')
    blogs = None
    if catagory_id:
        blogs = Blog.get_blog_by_catagory_id(catagory_id)
    else:
        blogs = Blog.objects.all()
    return {'catagory':all_catagory , 'blog_list':blogs}