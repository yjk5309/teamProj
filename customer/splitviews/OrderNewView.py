from .common import *

def OrderNewView (request):

    if request.method == 'POST':
        store = request.POST.get("store")
        book = request.POST.get("book")

        storeIdSql = "SELECT id FROM bookstore where store_name=(%s)"
        store_id = execute_and_get(storeIdSql, (store,))

        isbnSql = "SELECT book_isbn FROM book_inven " \
                  "where book_name = (%s) and store_id = (%s)"
        isbn = execute_and_get(isbnSql, (book, store_id,))

        price = request.POST.get("price")
        name = request.POST.get("new_name")
        address = request.POST.get("new_address")
        p_num = request.POST.get("new_p_number")
        e_mail = request.POST.get("new_e_mail")
        memo = request.POST.get("new_memo")

        user_id = request.user

        orderSql = "INSERT INTO order_info(user_id, store_id, isbn, " \
                   "order_name, order_address, order_p_num, order_email, order_memo, total_price) " \
                   "VALUES ((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s))"

        execute(orderSql, (user_id, store_id, isbn, name, address, p_num, e_mail, memo, price))

        return redirect('customer:main')