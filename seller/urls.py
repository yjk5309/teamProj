from django.urls import re_path
from .splitviews import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'seller'

urlpatterns = [
    re_path(r'^$', MainView, name='main'),
    re_path(r'^product_register/$', ProductRegisterView, name='product_register'),
    re_path(r'^book-ajax/$', SearchBookAjaxView, name='ajax_book_search'),
    re_path(r'^book_register/$', BookRegisterView, name='book_register'),
    re_path(r'^order/$', OrderCheckView, name='order_check'),
    re_path(r'^pay-check-ajax/(?P<order_num>\d+)/$', PayCheckAjaxView, name='pay_check_ajax'),
    re_path(r'^order-detail-ajax/(?P<order_num>\d+)/$', OrderDetailView, name='order_detail_ajax'),
    re_path(r'^order-return/$', OrderReturnView, name='order_return'),
    re_path(r'^order-return-check-ajax/(?P<return_id>\d+)/$', OrderReturnCheckAjaxView, name='order_return_check_ajax'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)