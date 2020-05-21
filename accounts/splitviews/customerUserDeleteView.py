from .common import *

@login_required
def customerUserDelete(request):
    user = request.user
    if request.method == "GET":
        return render(request, 'customerUserDelete.html')

    elif request.method == "POST":
        user_id = request.POST.get('id')
        user_password = request.POST.get('password')

        if user.username == user_id and user.check_password(user_password):
            user.delete()
            return redirect('customer:main')
        else:
            return redirect('accounts:customerMypage')

