from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Account
from django.db.models import Q
import json



@login_required
def addView(request):
    
    user = User.objects.get(username=request.user) 
    account = Account.objects.create(owner=user, iban=request.POST.get("iban"))
    account.save()

    return redirect("/")


@login_required
def homePageView(request):
    
    accounts = Account.objects.filter(owner=request.user)
    return render(request, "pages/index.html", {"accounts": accounts})