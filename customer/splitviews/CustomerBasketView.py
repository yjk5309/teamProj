from .common import *

@login_required
def CustomerBasketView(request):
    return render(request, 'book_basket.html')