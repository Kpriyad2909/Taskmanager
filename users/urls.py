# users/urls.py
from django.urls import path
from . import views
#from django.contrib.auth.views import (LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView)

app_name = 'users'

urlpatterns = [
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('signup/', views.sign_up, name='signup'),
    #path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'),name='password-reset'),
    #path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    #path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    #path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
    path('', views.home, name='home'),
]#