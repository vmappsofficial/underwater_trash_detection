import datetime
from urllib import request
from django.views.decorators.csrf import csrf_exempt
import traceback

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User, Group
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render, redirect

from myapp.models import Notification, Registration, Review, Issue_report, Upload, Detection


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
    print(username, password)
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request, user)
        if user.groups.filter(name='users').exists():
            return  JsonResponse(
                {
                    'status': 'ok',
                    'lid':user.id,
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
@csrf_exempt
# def user_signup_post(request):
#     # Only accept POST
#     if request.method != 'POST':
#         return JsonResponse({'status': 'error', 'message': 'Only POST allowed'}, status=405)
#
#     try:
#         # Use .get to avoid KeyError
#         name1 = request.POST.get('name1', '').strip()
#         email1 = request.POST.get('email1', '').strip()
#         phone_number1 = request.POST.get('phone_number1', '').strip()
#         dob1 = request.POST.get('dob1', '').strip()
#         place1 = request.POST.get('place1', '').strip()
#         gender1 = request.POST.get('gender1', '').strip()
#         city1 = request.POST.get('city1', '').strip()
#         state1 = request.POST.get('state1', '').strip()
#         pincode1 = request.POST.get('pincode1', '').strip()
#         password = request.POST.get('password1', '')
#         confirm_password = request.POST.get('_confirmPassword', '')
#
#         # Validate required fields
#         if not email1:
#             return JsonResponse({'status': 'error', 'message': 'Email required'}, status=400)
#         if not password:
#             return JsonResponse({'status': 'error', 'message': 'Password required'}, status=400)
#         if password != confirm_password:
#             return JsonResponse({'status': 'error', 'message': 'Passwords do not match'}, status=400)
#
#         photo = request.FILES.get('photo', None)
#
#         # Save photo only if provided
#         photo_path = ''
#         if photo:
#             fs = FileSystemStorage()
#             date = datetime.datetime.now().strftime('%d%M%Y-%H%M%S') + '.jpg'
#             fs.save(date, photo)
#             photo_path = fs.path(date)
#
#         # Create new auth user — ensure username uniqueness
#         # We use email as username (as your original code)
#         if User.objects.filter(username=email1).exists():
#             return JsonResponse({'status': 'error', 'message': 'User with this email already exists'}, status=400)
#
#         au = User.objects.create_user(username=email1, password=password)
#         try:
#             au_grp = Group.objects.get(name='users')
#             au.groups.add(au_grp)
#         except Group.DoesNotExist:
#             # If group missing, continue but warn
#             print("Group 'users' not found, skipping group assignment")
#
#         # Create registration object
#         r = Registration()
#         r.name = name1
#         r.photo = photo_path  # adjust if Registration.photo is a FileField - prefer saving to that field
#         r.phone = phone_number1
#         r.dob = dob1
#         r.email = email1
#         r.gender = gender1
#         r.place = place1
#         r.city = city1
#         r.state = state1
#         r.pincode = pincode1
#         r.USER = au
#         r.save()
#
#         return JsonResponse({'status': 'ok', 'message': 'User registered'})
#     except Exception as e:
#         # Log the stack trace to console (debug)
#         traceback.print_exc()
#         return JsonResponse({'status': 'error', 'message': 'Server error: ' + str(e)}, status=500)


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

    au=User.objects.create_user(username=email1,password=password)
    au.groups.add(Group.objects.get(name='users'))


    r=Registration()
    r.name=name1
    r.photo="/media/"+date
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

@csrf_exempt
# def view_profile(request):
#     if request.method == "POST":
#         lid = request.POST.get("lid")
#
#         if not lid or not lid.isdigit():
#             return JsonResponse({"status": "error", "message": "Invalid lid"}, status=400)
#
#         try:
#             user = User.objects.get(id=int(lid))
#             return JsonResponse({
#                 "status": "ok",
#                 "name": user.name,
#                 "dob": user.dob,
#                 "gender": user.gender,
#                 "email": user.email,
#                 "phone": user.phone,
#                 "place": user.place,
#                 "state": user.state,
#                 "pin": user.pin,
#                 "district": user.district,
#                 "photo": user.photo.url if user.photo else ""
#             })
#         except User.DoesNotExist:
#             return JsonResponse({"status": "error", "message": "Not Found"}, status=404)

def view_profile(request):
    id=request.POST['lid']
    user=Registration.objects.get(USER_id=id)
    return JsonResponse(
        {
            'status': 'ok',
            "name": user.name,
             "dob": user.dob,
            "gender": user.gender,
            "email": user.email,
           "phone": user.phone,
            "place": user.place,
            "state": user.state,
            "city": user.city,
            "pin": user.pincode,
            "photo": user.photo
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
    obj=Registration.objects.get(USER_id=lid)

    if 'photo' in request.FILES:
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime('%d%M%Y-%H%M%S') + '.jpg'
        fs.save(date, photo)
        obj.photo="/media/"+date
        obj.save()



    obj.name=name1
    obj.phone=phone_number1
    obj.dob=dob1
    obj.email=email1
    obj.gender=gender1
    obj.city=city1
    obj.state=state1
    obj.pincode=pincode1
    obj.save()
    return JsonResponse(
        {
            'status': 'ok',


        }
    )

# def user_change_password(request):
#     currentPassword = request.POST['current_password']
#     newPassword = request.POST['new_password']
#     confirmPassword = request.POST['confirm_password']
#     if newPassword != confirmPassword:
#         return JsonResponse(
#             {
#                 'status': 'error',
#             }
#         )
#     else:
#         lid = request.POST['lid']
#         d = User.objects.get(id=lid)
#         a = Registration.objects.get(USER_id=lid)
#         if
#         d.password=make_password(newPassword)
#         d.save()
#         return JsonResponse(
#             {
#                 'status': 'ok',
#             }
#         )
#
# def user_change_password(request):
#     id=request.POST['lid']
#     current_password = request.POST['current_password']
#     print(current_password)
#     new_password = request.POST['new_password']
#     confirm_password = request.POST['confirm_password']
#
#     # user=User.objects.get(id=id)
#     user=Registration.objects.get(USER_id=id)
#
#     if new_password==confirm_password:
#         if check_password(user.password,current_password):
#             user.set_password(new_password)
#             logout(request)
#             user.save()
#             return JsonResponse({'status': 'ok'})
#         else:
#             return JsonResponse({'status': 'no'})
#     else:
#         return JsonResponse({'status': 'no'})

  # Adjust to your actual model path

def user_change_password(request):

        id = request.POST['lid']
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']


        user = User.objects.get(id=id)

        if new_password != confirm_password:
            return JsonResponse({'status': 'no'})

        if not check_password(current_password,user.password ):
             return JsonResponse({'status': 'no'})

        user.set_password(new_password)
        user.save()
        logout(request)
        return JsonResponse({'status': 'ok'})





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


def view_detection(request):
    id= request.POST['id']
    print(id,"===========================")
    d = Detection.objects.filter(d_id=id)

    li=[]

    for item in d:
        li.append(
            {
                'id':item.id,
                'trash':item.trash,

            }
        )
    return JsonResponse(
        {
            'status': 'ok',
            'data':li
        }
    )





def view_upload(request):
    lid= request.POST['lid']
    d = Upload.objects.filter(REGISTRATION__USER_id=lid)

    li=[]

    for item in d:
        li.append(
            {
                'id':item.id,
                'uploaded_file':item.uploaded_file,
                'date':item.date,
            }
        )

    print(li)
    return JsonResponse(
        {
            'status': 'ok',
            'data':li
        }
    )




def upload_image(request):
    id=request.POST['id']
    photo = request.FILES['photo']
    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime('%d%M%Y-%H%M%S') + '.jpg'
    fs.save(date, photo)
    path = fs.url(date)
    data = Upload()
    data.uploaded_file=path
    data.date=datetime.datetime.now().today()
    data.REGISTRATION = Registration.objects.get(USER_id=id)
    data.save()

    return JsonResponse({
        'status': 'ok',
    })


