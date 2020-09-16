from .common import *

@login_required

def OrderCreateView (request):

    if request.method == 'POST':

        name = request.POST.get("name")
        address = request.POST.get("address")
        p_num = request.POST.get("p_number")
        e_mail = request.POST.get("e_mail")
        memo = request.POST.get("memo")
        payment = request.POST.get("payment")
        order_num = request.POST.get("date")

        user_id = request.user

        orderSql = "INSERT INTO order_info(user_id, order_name, " \
                   "order_address, order_p_num, order_email, order_memo, payment, order_num) " \
                   "VALUES ((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s))"
        execute(orderSql, (user_id, name, address, p_num, e_mail, memo, payment, order_num,))

        if len(order_num) != 0:
            store = request.POST.getlist("store")
            book = request.POST.getlist("book")
            price = request.POST.getlist("price")

            if len(store) >= 2:
                for i in range(len(store)):
                    storeIdSql = "SELECT id FROM bookstore where store_name=(%s)"
                    store_id = execute_and_get(storeIdSql, (store[i],))

                    isbnSql = "SELECT book_isbn FROM book_inven " \
                              "where book_name = (%s) and store_id = (%s)"
                    isbn = execute_and_get(isbnSql, (book[i], store_id,))

                    if payment in "bank":
                        listSql = "INSERT INTO order_products(order_num, store_id, isbn, price, order_status) " \
                                  "VALUES ((%s),(%s),(%s),(%s),(%s))"
                        execute(listSql, (order_num, store_id, isbn, price[i], '결제 대기중',))

                    elif payment in "card":
                        listSql = "INSERT INTO order_products(order_num, store_id, isbn, price, order_status) " \
                                  "VALUES ((%s),(%s),(%s),(%s),(%s))"
                        execute(listSql, (order_num, store_id, isbn, price[i], '결제 완료',))

            else:
                storeIdSql = "SELECT id FROM bookstore where store_name=(%s)"
                store_id = execute_and_get(storeIdSql, (store,))

                isbnSql = "SELECT book_isbn FROM book_inven " \
                          "where book_name = (%s) and store_id = (%s)"
                isbn = execute_and_get(isbnSql, (book, store_id,))

                if payment in "bank":

                    listSql = "INSERT INTO order_products(order_num, store_id, isbn, price, order_status) " \
                              "VALUES ((%s),(%s),(%s),(%s),(%s))"
                    execute(listSql, (order_num, store_id, isbn, price, '결제 대기중',))

                elif payment in "card":
                    listSql = "INSERT INTO order_products(order_num, store_id, isbn, price, order_status) " \
                              "VALUES ((%s),(%s),(%s),(%s),(%s))"
                    execute(listSql, (order_num, store_id, isbn, price, '결제 완료',))

            return redirect('customer:order_confirm', order_num = order_num)