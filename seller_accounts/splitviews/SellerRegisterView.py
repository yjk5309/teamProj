from .common import *
from customer_accounts.models import Seller

def SellerRegisterView(request):
    if request.method == "GET":
        return render(request, 'seller_register.html')

    elif request.method == "POST":
        name = request.POST.get("name")
        user_id = request.POST.get("user_id")
        user_pw = request.POST.get("user_pw")
        user_2nd_pw = request.POST.get("user_2nd_pw")
        business_number = request.POST.get("business_num")

        try:
            user = User.objects.get(username=user_id)
            if user.seller.business_number == business_number or user == User.objects.get(username=user_id):
                messages.error(request, "이미 존재하는 계정입니다.")
                return redirect('seller_accounts:seller_register')

        except ObjectDoesNotExist:
            if user_pw == user_2nd_pw:
                new_user = User.objects.create_user(first_name=name, username=user_id, password=user_pw)
                new_user.is_seller = True
                new_user.save()
                user = User.objects.get(username=user_id)
                user.seller.business_number = business_number
                user.save()

                messages.success(request, "회원가입에 성공하였습니다.")
                return redirect('customer_accounts:login')

            else:
                messages.error(request, "비밀번호가 일치하지 않습니다.")
                return redirect('seller_accounts:seller_register')