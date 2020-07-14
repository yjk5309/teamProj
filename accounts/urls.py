from django.urls import re_path
from .splitviews import *

app_name = 'accounts'

urlpatterns = [
    re_path(r'^customerLogin/$', CustomerLoginView, name='customerLogin'),
    re_path(r'^customerRegister/$', CustomerRegisterView, name='customerRegister'),
    re_path(r'^customerInfoModify/$', CustomerInfoModifyView, name='customerInfoModify'),
    re_path(r'^customerPasswordModify/$', CustomerPasswordModifyView, name='customerPasswordModify'),
    re_path(r'^customerLogout/$', CustomerLogoutView, name='customerLogout'),
    re_path(r'^customerMypage/$', CustomerMyPageView, name='customerMyPage'),
    re_path(r'^customerPasswordCheck/$', CustomerPasswordCheckView, name='customerPasswordCheck'),
    re_path(r'^customerUserDelete/$', CustomerUserDeleteView, name='customerUserDelete'),
]