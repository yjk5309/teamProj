from django.urls import re_path
from .splitviews import *

app_name = 'accounts'

urlpatterns = [
    re_path(r'^login/$', CustomerLoginView, name='customer_login'),
    re_path(r'^register/$', CustomerRegisterView, name='customer_register'),
    re_path(r'^info-modify/$', CustomerInfoModifyView, name='customer_info_modify'),
    re_path(r'^password-modify/$', CustomerPasswordModifyView, name='customer_password_modify'),
    re_path(r'^logout/$', CustomerLogoutView, name='customer_logout'),
    re_path(r'^mypage/$', CustomerMyPageView, name='customer_my_page'),
    re_path(r'^password-check/$', CustomerPasswordCheckView, name='customer_password_check'),
    re_path(r'^user-delete/$', CustomerUserDeleteView, name='customer_user_delete'),
]