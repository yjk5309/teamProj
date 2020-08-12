from .common import *

@login_required
def MyPageView(request):
    basket = book_basket

    return render(request,'mypage.html', {'basket':basket})