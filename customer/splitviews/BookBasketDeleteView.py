from .common import *

def BookBasketDeleteView(request, book_isbn):
    basket = book_basket
    tab = 'basket'

    if len(basket) == 1:
        del basket[0]

    for i in range(len(basket)-1):
        if basket[i]['isbn'] == book_isbn:
            del basket[i]

    return render(request, 'mypage.html', {'tab': tab, 'basket': basket})