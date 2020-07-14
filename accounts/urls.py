from django.urls import re_path
from .splitviews import *

app_name = 'accounts'

urlpatterns = [
    re_path(r'^customerLogin/$', CustomerLoginView, name='CustomerLogin'),
    re_path(r'^customerRegister/$', CustomerRegisterView, name='CustomerRegister'),
    re_path(r'^customerInfoModify/$', CustomerInfoModifyView, name='CustomerInfoModify'),
    re_path(r'^customerPasswordModify/$', CustomerPasswordModifyView, name='CustomerPasswordModify'),
    re_path(r'^customerLogout/$', CustomerLogoutView, name='CustomerLogout'),
    re_path(r'^customerMypage/$', CustomerMypageView, name='CustomerMyPage'),
    re_path(r'^customerPasswordCheck/$', CustomerPasswordCheckView, name='CustomerPasswordCheck'),
    re_path(r'^customerUserDelete/$', CustomerUserDeleteView, name='CustomerUserDelete'),
]