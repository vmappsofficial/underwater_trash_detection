from urllib import request

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect

from myapp.models import Notification, Registration


# Create your views here.

def admin_home(request):
    return render(request, 'admin_homepage.html')
def admin_login(request):
    return render(request, 'admin_login.html')
def admin_login_post(request):
    username = request.POST['username']
    password = request.POST['password']
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request, user)
        if user.groups.filter(name='admin').exists():
            messages.success(request, 'You are now logged in as admin')
            return redirect('/myapp/admin_home/')
        else:
            messages.error(request,'Invalid user')
            return redirect('/myapp/admin_login/')
    else:
        messages.error(request,'User not found')
        return redirect('/myapp/admin_login/')

def notification_post(request):
    date=request.POST['date']
    notification=request.POST['notification']
    a = Notification()
    a.date = date
    a.notification = notification
    a.save()
    messages.success(request,'Notification added')
    return redirect('/myapp/admin_home/')


def change_password_post(request):
    old_password = request.POST['password1']
    new_password = request.POST['password2']
    confirm_password = request.POST['password3']

    if check_password(old_password,request.user.password):
        if new_password == confirm_password:
            user = request.user
            user.set_password(new_password)
            user.save()
            messages.success(request,'Password changed successfully')
            return redirect('/myapp/admin_login/')
        else:
            messages.error(request,'Passwords do not match')
            return redirect('/myapp/admin_home/')
    else:
        messages.error(request,'Passwords do not match')
        return redirect('/myapp/admin_home/')

def forgot_password_post(request):
    email = request.POST['email']
    return


def review(request):
    return render(request, 'View_more.html')
def trash_detection_page(request):
    return render(request,'trash_detection.html')
def user_details(request):
    return render(request,'User_details.html')
def review_page(request):
    return render(request,'Review_page.html')
def password_page(request):
    return render(request,'password_page.html')
def forgot_password(request):
    return render(request,'password_page2.html')
def notifications(request):
    return render(request,'notification_page.html')

def user_login_post(request):
    username = request.POST['email1']
    password = request.POST['password1']
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request, user)
        if user.groups.filter(name='user').exists():
            return  JsonResponse(
                {
                    'status': 'ok',
                }
            )
        else:
            return JsonResponse(
                {
                    'status': 'no',
                }
            )
    else:
        messages.error(request, 'User not found')
        return redirect('/myapp/admin_login/')


def user_signup_post(request):
    name1 = request.POST['name1']
    email1 = request.POST['email1']
    phone_number1 = request.POST['phone_number1']
    dob1 = request.POST['dob1']
    place1 = request.POST['place1']
    gender1 = request.POST['gender1']
    city1 = request.POST['city1']
    state1 = request.POST['state1']
    pincode1 = request.POST['pincode1']
    password1 = request.POST['password1']
    au=User.objects.create_user(username=email1,password=password1)
    r=Registration()
    r.name=name1
    r.photo=""
    r.phone = phone_number1
    r.dob = dob1
    r.email = email1
    r.gender = gender1
    r.city = city1
    r.state = state1
    r.pincode = pincode1
    r.USER=au
    r.save()
    return JsonResponse(
        {
            'status': 'ok',
        }
    )

def view_profile(request):
    lid = request.POST['lid']
    d=Registration.objects.get(USER_id=lid)
    return  JsonResponse(
        {
            'status': 'ok',
            'photo': d.photo,
            'name':d.name,
            'phone':d.phone,
            'dob':d.dob,
            'email':d.email,
            'gender':d.gender,
            'city':d.city,
            'state': d.state,
            'pincode': d.pincode,
        }
    )
