from .common import *

def customerLoginView(request):
    if request.method == "GET":
        return render(request, 'customerLogin.html')

    elif request.method == "POST":
        user_id = request.POST.get("user_id")
        user_pw = request.POST.get("user_pw")

        login_user = authenticate(request, username=user_id, password=user_pw)

        if login_user is not None:
            login(request, login_user)
            return redirect('accounts:customerInfoModify')

        else:
            messages.error(request,'ID 혹은 비밀번호 오류입니다.')
            return redirect('accounts:customerLogin')
