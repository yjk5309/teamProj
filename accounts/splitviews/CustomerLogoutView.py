from .common import *

def CustomerLogoutView(request):
    logout(request)
    return redirect('customer:main')