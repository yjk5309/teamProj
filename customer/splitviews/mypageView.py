from .common import *

@login_required
def mypageView(request):
    return render(request,'mypage.html')