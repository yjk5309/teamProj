from django.urls import re_path
from .splitviews import *

app_name = 'customer'

urlpatterns = [
    re_path(r'^main/$', MainView, name='main'),
    re_path(r'^search_store/$', SearchStoreView, name='search_store'),
    re_path(r'^searchBook/$', SearchBookView, name='searchBook'),
    re_path(r'^searchBookResult/$', SearchBookResultView, name='searchBookResult'),
    re_path(r'^mypage/$', mypageView, name='mypage'),
]
