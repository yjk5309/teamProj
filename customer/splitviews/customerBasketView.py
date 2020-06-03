from .common import *

@login_required
def customerBasketView(request):
    return render(request, 'customer_basket.html')