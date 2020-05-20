from .common import *

@login_required
def customerPasswordCheck(request):
    user = request.user

    if request.method == "GET":
        return render(request, 'customerPasswordCheck.html')

    elif request.method == "POST":
        password = request.POST.get('password')

        if user.check_password(password):
            return redirect('accounts:customerMypage')
        else:
            return redirect('accounts:customerPasswordCheck')