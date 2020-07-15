from django.urls import re_path
from .splitviews import *

app_name = 'accounts'

urlpatterns = [
    re_path(r'^customerLogin/$', CustomerLoginView, name='customer_login'),
    re_path(r'^customerRegister/$', CustomerRegisterView, name='customer_register'),
    re_path(r'^customerInfoModify/$', CustomerInfoModifyView, name='customer_info_modify'),
    re_path(r'^customerPasswordModify/$', CustomerPasswordModifyView, name='customer_password_modify'),
    re_path(r'^customerLogout/$', CustomerLogoutView, name='customer_logout'),
    re_path(r'^customerMypage/$', CustomerMyPageView, name='customer_my_page'),
    re_path(r'^customerPasswordCheck/$', CustomerPasswordCheckView, name='customer_password_check'),
    re_path(r'^customerUserDelete/$', CustomerUserDeleteView, name='customer_user_delete'),
]