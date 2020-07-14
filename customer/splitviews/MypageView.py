from .common import *

@login_required
def MypageView(request):
    return render(request,'mypage.html')