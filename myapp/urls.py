
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('admin_home/',views.admin_home),
    path('admin_login/',views.admin_login),
    path('view_more/',views.review),
    path('trash_detection/',views.trash_detection_page),
    path('user_details/',views.user_details),
    path('Review_page/',views.review_page),
    path('Password_change/',views.password_page),
    path('Forgot_password/',views.forgot_password),
    path('notifications/',views.notifications),
    path('notification_post/',views.notification_post),
    path('admin_login_post/',views.admin_login_post),
    path('change_password_post/',views.change_password_post),
    path('forgot_password_post/',views.forgot_password_post),
    path('user_login_post/',views.user_login_post),
    path('user_signup_post/',views.user_signup_post),
    path('view_profile/',views.view_profile),
    path('edit_profile/',views.edit_profile_post),
    path('upload_image/',views.upload_image),



]
