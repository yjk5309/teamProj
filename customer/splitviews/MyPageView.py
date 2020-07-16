from .common import *

@login_required
def MyPageView(request):
    return render(request,'mypage.html')