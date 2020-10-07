from .common import *

@login_required

def BookStoreRegisterView(request):
    if request.method == "GET":
        return render(request, 'bookstore_registration.html')

    elif request.method == "POST":
        user = request.user

        store_name = request.POST.get("store_name")
        repre_name = request.POST.get("repre_name")

        address = request.POST.get("address")
        store_number = request.POST.get("store_number")
        store_email = request.POST.get("e_mail")
        store_msg = request.POST.get("store_msg")

        store_img = request.FILES.get('store_img')

        store_img_url = fileUpload(user, store_img)

        orderSql = "INSERT INTO bookstore(store_name, repre_name, " \
                   "address, store_num, store_email, store_msg, bookstore_img, seller_id) " \
                   "VALUES ((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s))"
        execute(orderSql, (store_name, repre_name, address, store_number, store_email, store_msg, store_img_url, user))

        return redirect('customer:main')