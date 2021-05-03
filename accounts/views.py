from django.shortcuts import render
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm


@csrf_exempt
def signup(request):
    if request.method == 'GET':
        return render(request=request, template_name='signup.html')
    elif request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('User created successfully!')

        return HttpResponse(f'{form.errors}')


@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request=request, template_name='login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            dj_login(request, user)
            return HttpResponse('Login completed!')
        return HttpResponse('Wrong password/username')


@csrf_exempt
@login_required(login_url='/login/')
def logout(request):
    if request.method == 'POST':
        dj_logout(request)
        return HttpResponse('Logout successfully')

    return HttpResponse('Only post method allowed')


'''
@csrf_exempt
def change_password(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponse('Please login first')

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
