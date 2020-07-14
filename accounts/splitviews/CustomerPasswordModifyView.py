from .common import *

@login_required
def CustomerPasswordModifyView(request):
    user = request.user

    if request.method == "POST":
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        check_new_password = request.POST.get('check_new_password')

        if user.check_password(current_password):
            if user.check_password(new_password):
                messages.error(request, "새로운 비밀번호는 이전 비밀번호와 다르게 설정해주세요.")
                return redirect('accounts:customerMyPage')

            else:
                if new_password == check_new_password:
                    user.set_password(new_password)
                    user.save()

                    messages.success(request, "비밀번호 변경이 완료되었습니다. 다시 로그인해주세요.")
                    return redirect('accounts:customerLogin')

                else:
                    messages.error(request, "새로운 비밀번호가 서로 일치하지 않습니다.")
                    return redirect('accounts:customerMyPage')

        else:
            messages.error(request, "현재 비밀번호가 일치하지 않습니다.")
            return redirect('accounts:customerMyPage')

