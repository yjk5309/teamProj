from .common import *

@login_required
def SellerInfoView(request):
    tab_is = 0
    user = request.user
    storeSql = "SELECT store_name, address, store_num, bookstore_img, store_msg, store_email, repre_name " \
               "FROM bookstore WHERE seller_id = (%s)"
    data = execute_and_get(storeSql, (user,))

    if len(data) == 0 :
        messages.success(request, "마이페이지는 서점 등록 후 이용가능합니다.")
        return redirect('seller_accounts:bookstore_register')

    else:
        store = {'store_name': data[0][0],
                 'address': data[0][1],
                 'store_num': data[0][2],
                 'store_img': data[0][3],
                 'store_msg': data[0][4],
                 'store_email': data[0][5],
                 'repre_name': data[0][6],
                 }

        return render(request, 'seller_info.html', {'store':store, 'tab_is': tab_is})