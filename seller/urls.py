from django.urls import re_path
from .splitviews import *

app_name = 'seller'

urlpatterns = [
    re_path(r'^$', MainView, name='main'),
]