from django.contrib import admin
from django.urls import path, re_path
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    re_path(r'^accounts/', include('accounts.urls')),
    # re_path(r'^customer/', include('customer.urls')),
    # re_path(r'^seller/', include('seller.urls')),
=======
    #re_path(r'^accounts/', include('accounts.urls')),
    re_path(r'^customer/', include('customer.urls')),
    #re_path(r'^seller/', include('seller.urls')),
>>>>>>> befa97c495849fe7218815bd2796cc150c484e0e
]
