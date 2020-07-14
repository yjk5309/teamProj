from .common import *

@login_required
def CustomerBasketView(request):
    return render(request, 'customer_basket.html')