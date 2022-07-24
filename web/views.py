#from asyncio.windows_events import NULL
import json
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
import requests
from django.contrib.auth import login as logina, authenticate,logout

from darbinieki.forms import LoginForm
def sakumlapa(request):
    return render(request, "homepage.html", {"title":"Sākumlapa"})

def api_tests_universitates(request):
    return render(request, "pages/api_uni_frontpage.html", {"title":"Api - Universitātes"})
def login(request):
    form = LoginForm()
    message =''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                logina(request, user)
                next_url = request.GET.get('next')
                if next_url:
                    return HttpResponseRedirect(next_url)
                else:
                    return redirect('/')
            else:
                message = 'Login failed!'
    return render(request, "../templates/pages/login.html", {"form":form,"title":"Login","msg":message})

def iziet(request):
    logout(request)
    return redirect('/')
def nav_piekluves(request):
    return render(request, "../templates/pages/nav_piekluves.html", {"title":"Nav piekļuves"})
