from django.urls import re_path
from .splitviews import *

app_name = 'customer'

urlpatterns = [
    re_path(r'^$', MainView, name='main'),
    re_path(r'^search_store/$', SearchStoreView, name='search_store'),
    re_path(r'^searchBook/$', SearchBookView, name='searchBook'),
    re_path(r'^searchBookResult/$', SearchBookResultView, name='searchBookResult'),
    re_path(r'^mypage/$', mypageView, name='mypage'),
    re_path(r'^ajax_get_region2/$', AjaxGetRegion2View, name='ajax_get_region2'),
]
