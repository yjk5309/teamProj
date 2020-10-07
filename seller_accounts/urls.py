from django.urls import re_path
from .splitviews import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'seller_accounts'

urlpatterns = [
    re_path(r'^seller_register/$', SellerRegisterView, name='seller_register'),
    re_path(r'^bookstore_register/$', BookStoreRegisterView, name='bookstore_register'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)