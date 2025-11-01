
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
    path('user_change_password/',views.user_change_password),
    path('view_upload_file/',views.view_upload),
    path('view_detections/',views.view_detection),
    path('user_forgot_password/',views.user_forgot_password),
    path('send_review/',views.send_review),
    path('admin_view_review/',views.admin_view_review),
    path('user_view_review/',views.user_view_review),
    path('user_view_notifications/',views.user_view_Notification),
    path('report_issue/',views.report_issue),
    path('view_issue/',views.view_issues),
    path('adminSend_reply/<id>', views.adminSend_reply),
    path('admin_sendAction/',views.admin_sendAction),
    path('user_view_issue/',views.user_view_issue),




]
