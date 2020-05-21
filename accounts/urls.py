from django.urls import re_path
from .splitviews import *

app_name = 'accounts'

urlpatterns = [
    re_path(r'^customerLogin/$', customerLoginView, name='customerLogin'),
    re_path(r'^customerRegister/$', customerRegisterView, name='customerRegister'),
    re_path(r'^customerInfoModify/$', customerInfoModify, name='customerInfoModify'),
    re_path(r'^customerPasswordModify/$', customerPasswordModify, name='customerPasswordModify'),
    re_path(r'^customerLogout/$', customerLogout, name='customerLogout'),
    re_path(r'^customerMypage/$', customerMypage, name='customerMypage'),
    re_path(r'^customerPasswordCheck/$', customerPasswordCheck, name='customerPasswordCheck'),
    re_path(r'^customerUserDelete/$', customerUserDelete, name='customerUserDelete'),
]