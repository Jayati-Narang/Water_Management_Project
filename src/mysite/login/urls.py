from django.urls import path
from login import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout')
    
    
]
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
#
# urlpatterns = [
#     path('', views.signup, name='signup')
# ]
