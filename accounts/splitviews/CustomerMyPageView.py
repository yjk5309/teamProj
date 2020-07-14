from .common import *

@login_required
def CustomerMyPageView(request):
    return render(request, 'customer_my_page.html')