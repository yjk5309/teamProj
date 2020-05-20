from .common import *

@login_required
def customerMypage(request):
    return render(request, 'customerMypage.html')