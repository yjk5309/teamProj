from .common import *

@login_required
def CustomerUserDeleteView(request):
    user = request.user

    if request.method == "POST":
        user_id = request.POST.get('id')
        user_password = request.POST.get('password')

        if user.username == user_id and user.check_password(user_password):
            user.delete()
            messages.success(request,'회원탈퇴가 정상적으로 완료되었습니다.')
            return redirect('accounts:customer_login')
        else:
            messages.error(request, '입력하신 정보가 정확하지 않습니다.')
            return redirect('accounts:customer_my_page')

