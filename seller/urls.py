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
    re_path(r'^delivery/$', DeliveryCheckView, name='delivery_check'),
    re_path(r'^delivery-ajax/(?P<order_num>\d+)/$', DeliveryCheckAjaxView, name='delivery_check_ajax'),
    re_path(r'^settlement/$', SettlementCheckView, name='settlement_check'),
    re_path(r'^monthly-settlement/$', MonthlySettlementView, name='monthly_settlement'),
    re_path(r'^review/$', ReviewManageView, name='review_manage'),
    re_path(r'^review-answer/$', ReviewAnswerView, name='review_answer'),
    re_path(r'^review-answer-ajax/(?P<review_id>\d+)/$', AjaxGetReviewAnswerView, name='answer_modify_ajax'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)