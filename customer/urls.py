from django.urls import re_path
from .splitviews import *

app_name = 'customer'

urlpatterns = [
    re_path(r'^$', MainView, name='Main'),
    re_path(r'^search_store/$', SearchStoreView, name='SearchStore'),
    re_path(r'^searchBook/$', SearchBookView, name='SearchBook'),
    re_path(r'^searchBookResult/$', SearchBookResultView, name='SearchBookResult'),
    re_path(r'^mypage/$', MypageView, name='MyPage'),
    re_path(r'^ajax_get_city/$', AjaxGetCityView, name='AjaxGetCity'),
]
