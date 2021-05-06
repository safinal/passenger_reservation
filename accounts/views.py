from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm


@csrf_exempt
def signup(request):
    if request.user.is_authenticated:
        return redirect('/train/')
    elif request.method == 'GET':
        return render(request=request, template_name='accounts/index.html', context={'form_errors': False})
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/train/')
        return render(request=request, template_name='accounts/index.html', context={'form_errors': f'{form.errors}'})


@csrf_exempt
def login(request):
    if request.user.is_authenticated:
        return redirect('/train/')
    elif request.method == 'GET':
        return render(request=request, template_name='accounts/login.html', context={'wrong': False})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            dj_login(request, user)
            return redirect('/train/')
        return render(request=request, template_name='accounts/login.html', context={'wrong': True})


@csrf_exempt
@login_required(login_url='/login/')
def logout(request):
    if request.method == 'POST':
        dj_logout(request)
        return redirect(to='/login/')
