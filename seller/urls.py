from django.urls import re_path
from .splitviews import *

app_name = 'seller'

urlpatterns = [
    re_path(r'^$', MainView, name='main'),
    re_path(r'^product/$', ProductListView, name='product_list'),
    re_path(r'^product/book-list$', SearchBookInManageView, name='search_book_in_manage'),
    re_path(r'^product/book-delete/(?P<store_id>\d+)/(?P<isbn>\d+)/$', ProductDeleteView, name='book_delete'),
]