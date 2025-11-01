import datetime
import smtplib
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
from django.contrib import messages
from django.contrib.auth.models import User
import smtplib
import random

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
    data = Detection.objects.all()
    return render(request,'trash_detection.html',{'data':data},)
def user_details(request):
    data = Registration.objects.all()
    return render(request,'User_details.html',{'data':data})
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
    photo = request.FILES['photo']
    lid=request.POST['lid']
    description=request.POST['description']
    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime('%d%M%Y-%H%M%S') + '.jpg'
    fs.save(date, photo)
    path=fs.url(date)
    R = Issue_report()
    R.latitude=latitude
    R.longitude=longitude
    R.description=description
    R.photo=path
    R.date=datetime.datetime.now().today()
    R.Registration= Registration.objects.get(USER_id=lid)
    R.action='pending'
    R.save()
    return JsonResponse(
        {
            'status': 'ok',
        }
    )
def view_user_issue(request):
    id=request.POST['lid']
    a=Issue_report.objects.filter(Registration_USER_id=id)
    l=[]
    for i in a:
        l.append({
            'photo': i.photo,
            'latitude': i.latitude,
            'longitude': i.longitude,
            'description': i.description,
            'date': i.date,
            'action': i.action,
        })
    return JsonResponse({'status': 'ok','data': l})

from django.shortcuts import render

from django.shortcuts import render
from .models import Issue_report
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
import logging

# Set up logging for geocoding errors
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def view_issues(request):
    issues = Issue_report.objects.all().order_by('-date')
    geolocator = Nominatim(user_agent="aquaclean_ai")  # Initialize geocoder
    issues_with_place = []

    for issue in issues:
        try:
            # Convert latitude and longitude to float
            lat = float(issue.latitude)
            lon = float(issue.longitude)
            # Perform reverse geocoding
            location = geolocator.reverse((lat, lon), language='en')
            place_name = location.address if location else "Unknown location"
        except (ValueError, GeocoderTimedOut, GeocoderUnavailable) as e:
            logger.error(f"Geocoding failed for lat: {issue.latitude}, lon: {issue.longitude} - Error: {str(e)}")
            place_name = "Unknown location"

        issues_with_place.append({
            'issue': issue,
            'place_name': place_name
        })

    return render(request, 'view_issue.html', {'issues_with_place': issues_with_place})
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

    ########

    # pip install ultralytics
    #             opencv-python

    from ultralytics import YOLO
    import cv2
    import math

    # Load your custom-trained model here (replace path accordingly)
    model = YOLO(r'C:\Users\hp\PycharmProjects\UnderWatertrash\60_epochs_denoised.pt')

    # Define your class names — should match your model's training classes
    classNames = ['mask', 'can', 'cellphone', 'electronics', 'glass-bottle', 'glow', 'metal', 'mise', 'net',
                  'plastic-bag', 'plastic-bottle', 'plastic', 'rod', 'sunglass', 'tyre']

    # Confidence threshold (lowered to 0.3 for better detection)
    confidence_threshold = 0.2

    # Path to input image
    image_path = r"C:\Users\hp\PycharmProjects\UnderWatertrash\media\\"+date

    # Read image
    img = cv2.imread(image_path)
    if img is None:
        print("⚠️ Failed to load image. Check the image path and file.")
        exit()

    # Run detection
    results = model(img)

    detected_classes = set()


    data = Upload()
    data.uploaded_file=path
    data.date=datetime.datetime.now().today()
    data.REGISTRATION = Registration.objects.get(USER_id=id)
    data.save()

    for r in results:
        boxes = r.boxes
        # Debug: print all detected class indices and confidences
        print("Detected classes (indices):", boxes.cls.cpu().numpy())
        print("Confidences:", boxes.conf.cpu().numpy())

        for box in boxes:

            print(box, "============")
            conf = float(box.conf[0])
            cls = int(box.cls[0])

            if conf >= confidence_threshold:
                print(cls, "detected")

                d=Detection()
                d.d=data
                d.trash=classNames[cls]
                d.save()

                # if cls < len(classNames):
                #     class_name = classNames[cls]
                #     detected_classes.add(class_name)

    # if detected_classes:
    #     print("Detected trash items in image:")
    #     for item in detected_classes:
    #         print(f"- {item}")
    # else:
    #     print("No trash items detected in the image.")

    ########








    return JsonResponse({
        'status': 'ok',
    })
from django.core.mail import send_mail
from django.conf import settings
def user_forgot_password(request):
    email = request.POST['email']

    user = User.objects.get(username=email)

    import random
    psw = random.randint(1000, 9999)
    send_mail("Temporary Password", str(psw), settings.EMAIL_HOST_USER, [email])
    user.set_password(str(psw))
    user.save()
    return JsonResponse({
        'status': 'ok',
    })


def send_review(request):
    id = request.POST['lid']
    review = request.POST['review']
    rating = request.POST['rating']
    obj = Review()
    obj.review=review
    obj.rating=rating
    obj.date= datetime.datetime.now().today()
    obj.Registration = Registration.objects.get(USER_id=id)
    obj.save()
    return JsonResponse({
        'status': 'ok',
    })

def admin_view_review(request):
    a=Review.objects.all()
    return render(request,'Review_page.html',{'data':a})
def user_view_review(request):
    id = request.POST['lid']
    print(id,'knkn')
    a=Review.objects.filter(Registration__USER_id=id)
    l=[]
    for i in a:
        l.append({
            'review':i.review,
            'rating':i.rating,
            'date':i.date,
        })
    return JsonResponse({
        'status': 'ok',
        'data':l,
    })




def forgot_password(request):
    return render(request, 'password_page2.html')

def forgot_password_post(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(f"Email received: {email}")  # Debug logging

        if not email:
            messages.error(request, 'Email is required')
            return redirect('/myapp/forgot_password/')

        if User.objects.filter(username=email).exists():
            try:
                # Generate random password
                new_pass = random.randint(10000, 99999)
                print(f"Generated password: {new_pass}")  # Debug logging

                # Send email
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login("rahulrajvm7491@gmail.com", 'jhmfelpyefonxeiu')  # App Password
                to = email
                subject = "Password Reset"
                body = f"Your new password is: {new_pass}\nPlease log in and change it immediately."
                msg = f"Subject: {subject}\n\n{body}"
                server.sendmail("rahulrajvm7491@gmail.com", to, msg)
                server.quit()
                print(f"Email sent to: {to}")  # Debug logging

                # Update user password
                user = User.objects.get(username=email)
                user.set_password(str(new_pass))
                user.save()
                print(f"Password updated for user: {email}")  # Debug logging

                messages.success(request, 'New password sent to your email')
                return redirect('/myapp/admin_login/')
            except Exception as e:
                print(f"Error sending email: {e}")  # Debug logging
                messages.error(request, f'Failed to send email: {str(e)}')
                return redirect('/myapp/forgot_password/')
        else:
            messages.warning(request, 'Email does not exist')
            return redirect('/myapp/forgot_password/')
    else:
        messages.error(request, 'Invalid request method')
        return redirect('/myapp/forgot_password/')

def user_view_Notification(request):
    a=Notification.objects.all()
    l=[]
    for i in a:
        l.append({
            'date':i.date,
            'notification':i.notification,
        })
    return JsonResponse({
        'status': 'ok',
        'data':l,
    })


def adminSend_reply(request,id):
    a=Issue_report.objects.get(id=id)
    return render(request, 'sendAction.html',{'data':a})
def admin_sendAction(request):
    id=request.POST['id']
    action=request.POST['action']
    obj=Issue_report.objects.get(id=id)
    obj.status='replaid'
    obj.action=action
    obj.save()
    return redirect('/myapp/view_issue/')


def user_view_issue(request):
    lid=request.POST['lid']
    print(lid)
    a=Issue_report.objects.filter(Registration__USER_id=lid)
    l=[]
    for i in a:
        l.append({
            'date':i.date,
            'photo':i.photo,
            'description':i.description,
            'action':i.action,
        })
    return JsonResponse({
        'status': 'ok',
        'data':l,
    })