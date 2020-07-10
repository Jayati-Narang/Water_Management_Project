# from django.conf.urls import url
# from mysite.signup import views as core_views
#
# urlpatterns = [
#     url(r'^signup/$', core_views.signup, name='signup')
# ]
from django.urls import path
from signup import views

urlpatterns = [
    path('', views.signup, name='signup')
]
