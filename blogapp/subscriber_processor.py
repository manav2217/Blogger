from django import forms
from blogapp.forms import SubscriberForm
from .models import *
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from .forms import *


def subscribers(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['sub_email']
            new_sub = Subscriber(sub_email=email)
            sub = Subscriber.objects.filter(sub_email=email).exists()
            if sub:
                messages.info(request , "Email Already Subscribed , Thank You")
            else:
                new_sub.save()
                messages.success(request, "Thank You for subscribing")
    else:
        form = SubscriberForm()

    return {'sub_form': form}

