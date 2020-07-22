from .common import *

def LoginView(request):
    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == "POST":
        user_id = request.POST.get("user_id")
        user_pw = request.POST.get("user_pw")

        login_user = authenticate(request, username=user_id, password=user_pw)

        if login_user is not None:
            login(request, login_user)
            return redirect('customer:main')

        else:
            messages.error(request,'ID 또는 비밀번호 오류입니다.')
            return redirect('customer_accounts:login')
