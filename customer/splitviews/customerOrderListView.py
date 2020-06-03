from .common import *

@login_required
def customerOrderListView(request):
    return render(request, 'customer_order_list.html')