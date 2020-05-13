from django.urls import re_path
from .splitviews import *

app_name = 'customer'

urlpatterns = [
    re_path(r'^main/$', MainView, name='main'),
]
