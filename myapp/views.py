import datetime
from urllib import request

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User, Group
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render, redirect

from myapp.models import Notification, Registration, Review, Issue_report, Upload


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
    username = request.POST['Username']
    password = request.POST['Password']
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request, user)
        if user.groups.filter(name='users').exists():
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
    print(name1,"------------------------")
    email1 = request.POST['email1']
    phone_number1 = request.POST['phone_number1']
    dob1 = request.POST['dob1']
    place1 = request.POST['place1']
    gender1 = request.POST['gender1']
    city1 = request.POST['city1']
    state1 = request.POST['state1']
    pincode1 = request.POST['pincode1']
    password = request.POST['password1']
    photo = request.FILES['photo']
    confirm_password = request.POST['_confirmPassword']

    if password!=confirm_password:
        return JsonResponse(
            {
                'status': 'error',
            }
        )

    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime('%d%M%Y-%H%M%S')+'.jpg'
    fs.save(date,photo)
    path = fs.path(date)

    au=User.objects.create_user(username=email1,password=password)
    au_grp = Group.objects.get(name='users')
    au.groups.add(au_grp)
    au_grp.save()

    r=Registration()
    r.name=name1
    r.photo=path
    r.phone = phone_number1
    r.dob = dob1
    r.email = email1
    r.gender = gender1
    r.place = place1
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


def edit_profile_post(request):
    name1 = request.POST['name1']
    email1 = request.POST['email1']
    phone_number1 = request.POST['phone_number1']
    dob1 = request.POST['dob1']
    place1 = request.POST['place1']
    gender1 = request.POST['gender1']
    city1 = request.POST['city1']
    state1 = request.POST['state1']
    pincode1 = request.POST['pincode1']
    lid = request.POST['lid']

    d = Registration.objects.get(USER_id=lid)
    d.name=name1
    d.phone=phone_number1
    d.dob=dob1
    d.email=email1
    d.gender=gender1
    d.city=city1
    d.state=state1
    d.pincode=pincode1
    d.save()
    return JsonResponse(
        {
            'status': 'ok',


        }
    )

def user_change_password(request):
    password1 = request.POST['current_password']
    password2 = request.POST['new_password']
    lid = request.POST['lid']
    d = User.objects.get(id=lid)
    d.password=make_password(password2)
    d.save()
    return JsonResponse(
        {
          'status': 'ok',
        }
    )

def review_post(request):
    review_content =request.POST['review']
    lid=request.POST['lid']
    rating=request.POST['rating']


    R=Review()
    R.rating=rating
    R.content=review_content
    R.date=  datetime.datetime.now()
    R.Registration= Registration.objects.get(USER_id=lid)
    R.save()

    return JsonResponse({
        'status': 'ok',

    })

def view_notification(request):
    d=Notification.objects.all()

    return JsonResponse(
        {
            'status': 'ok',
        }
    )

def view_review(request):
    d=Review.objects.all()
    return JsonResponse(
        {
            'status': 'ok',
        }
    )
def report_issue(request):
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
    lid=request.POST['lid']
    description=request.POST['description']
    action=request.POST['action']
    R = Issue_report()
    R.latitude=latitude
    R.longitude=longitude
    R.description=description
    R.date=datetime.datetime.now()
    R.Registration= Registration.objects.get(USER_id=lid)
    R.action=action
    R.save()
    return JsonResponse(
        {
            'status': 'ok',
        }
    )
def view_issue(request):
    lid= request.POST['lid']
    d = Issue_report.objects.filter(USER_id=lid)
    return JsonResponse(
        {
            'status': 'ok',
        }
    )
def upload_image(request):
    id=request.POST['id']
    photo = request.FILES['photo']
    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime('%d%M%Y-%H%M%S') + '.jpg'
    fs.save(date, photo)
    path = fs.path(date)
    data = Upload()
    data.photo=path
    data.date=datetime.datetime.now().today()
    data.REGISTRATION = Registration.objects.get(USER_id=id)
    data.save()




