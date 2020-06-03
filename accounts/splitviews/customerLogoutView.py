from .common import *

def customerLogout(request):
    logout(request)
    return redirect('customer:main')