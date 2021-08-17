import random
import string
from django.utils.text import slugify

def ranstring(N):
    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=N))
    return res

def genslug(text):
    newslug = slugify(text)
    from .models import Blog
    if Blog.objects.filter(slug = newslug).exists():
        newslug = genslug(text + ranstring(5))
    return  newslug
