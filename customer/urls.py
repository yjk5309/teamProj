from django.urls import re_path
from .splitviews import *

app_name = 'customer'

urlpatterns = [
    re_path(r'^$', MainView, name='main'),
    re_path(r'^bookstore/$', SearchStoreView, name='search_store'),
    re_path(r'^bookstore/region/$', RegionSearchView, name='region_search'),
    re_path(r'^bookstore/keyword/$', KeywordSearchView, name='keyword_search'),
    re_path(r'^book/$', SearchBookView, name='search_book'),
    re_path(r'^book-list/$', SearchBookResultView, name='search_book_result'),
    re_path(r'^mypage/$', MyPageView, name='mypage'),
    re_path(r'^ajax-city/$', AjaxGetCityView, name='ajax_get_city'),
    re_path(r'^book/(?P<book_id>\d+)/$', BookDetailView, name='book_detail'),
    re_path(r'^book/(?P<book_isbn>\d+)/customer/$', BookLikeView, name='book_like'),
]
