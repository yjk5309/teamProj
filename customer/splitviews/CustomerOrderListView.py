from .common import *

@login_required
def CustomerOrderListView(request):
    return render(request, 'customer_order_list.html')