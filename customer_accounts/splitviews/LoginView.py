from .common import *

def LoginView(request):
    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == "POST":
        user_id = request.POST.get("user_id")
        user_pw = request.POST.get("user_pw")

        login_user = authenticate(request, username=user_id, password=user_pw)

        if login_user is not None and login_user.user_type == 2:
            login(request, login_user)
            return redirect('customer:main')

        elif login_user is not None and login_user.user_type == 3:
            login(request, login_user)
            return redirect('seller_accounts:bookstore_register')

        else:
            messages.error(request,'ID 또는 비밀번호 오류입니다.')
            return redirect('customer_accounts:login')
