from .common import *

@login_required
def CustomerPasswordCheckView(request):
    user = request.user

    if request.method == "GET":
        return render(request, 'customer_password_check.html')

    elif request.method == "POST":
        password = request.POST.get('password')

        if user.check_password(password):
            return redirect('accounts:customerMyPage')
        else:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
            return redirect('accounts:customerPasswordCheck',)