from django.urls import re_path
from .splitviews import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'seller'

urlpatterns = [
    re_path(r'^$', MainView, name='main'),
    re_path(r'^product_register/$', ProductRegisterView, name='product_register'),
    re_path(r'^book-ajax/$', SearchBookAjaxView, name='ajax_book_search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)