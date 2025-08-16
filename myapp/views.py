from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from pyexpat.errors import messages


# Create your views here.

def admin_home(request):
    return render(request, 'admin_homepage.html')
def admin_login(request):
    return render(request, 'admin_login.html')
def admin_login_post(request):
    username = request.POST['username']
    password = request.POST['password']
    ll=authenticate(username=username,password=password)
    if ll is not None:
        login(request, ll)
        if ll.groups.filter(name='admin'):
            return redirect('/myapp/admin_home/')
        else:
            messages.error(request,'Invalid user')
            return redirect('/myapp/admin_login/')
    else:
        messages.error(request,'User not found')
        return redirect('/myapp/admin_login/')


def change_password_post(request):
    old_password = request.POST['password1']
    new_password = request.POST['password2']
    confirm_password = request.POST['password3']
    return
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