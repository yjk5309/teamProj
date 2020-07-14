from .common import *

@login_required
def CustomerMypageView(request):
    return render(request, 'customer_my_page.html')