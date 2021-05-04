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
        return render(request=request, template_name='signup.html', context={'form_errors': False})
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/train/')
        return render(request=request, template_name='signup.html', context={'form_errors': f'{form.errors}'})


@csrf_exempt
def login(request):
    if request.user.is_authenticated:
        return redirect('/train/')
    elif request.method == 'GET':
        return render(request=request, template_name='login.html', context={'wrong': False})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            dj_login(request, user)
            return redirect('/train/')
        return render(request=request, template_name='login.html', context={'wrong': True})


@csrf_exempt
@login_required(login_url='/login/')
def logout(request):
    if request.method == 'POST':
        dj_logout(request)
        return redirect(to='/login/')
    return HttpResponse('Only post method allowed')


'''
@csrf_exempt
@login_required(login_url='/login/')
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.get('new_password2')
        if not request.user.check_password(old_password):
            return HttpResponse('Wrong old password')
        if new_password1 != new_password2:
            return HttpResponse('Entered passwords are not identical')
        request.user.set_password(new_password1)
        request.user.save()
        return HttpResponse('Password changed successfully!')
    return HttpResponse('Only post method allowed')
'''
