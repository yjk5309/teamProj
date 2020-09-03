from .common import *

@login_required

def OrderCreateView (request):

    if request.method == 'POST':
        store = request.POST.get("store")
        book = request.POST.get("book")

        storeIdSql = "SELECT id FROM bookstore where store_name=(%s)"
        store_id = execute_and_get(storeIdSql, (store,))

        isbnSql = "SELECT book_isbn FROM book_inven " \
                  "where book_name = (%s) and store_id = (%s)"
        isbn = execute_and_get(isbnSql, (book, store_id,))

        price = request.POST.get("price")
        name = request.POST.get("name")
        address = request.POST.get("address")
        p_num = request.POST.get("p_number")
        e_mail = request.POST.get("e_mail")
        memo = request.POST.get("memo")

        user_id = request.user

        orderSql = "INSERT INTO order_info(user_id, store_id, isbn, " \
                   "order_name, order_address, order_p_num, order_email, order_memo, total_price) " \
                   "VALUES ((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s))"

        execute(orderSql, (user_id, store_id, isbn, name, address, p_num, e_mail, memo, price))

        order_data = {'price': price,
                      'book': book,
                      'name': name,
                      'address': address,
                      'p_num': p_num,
                      'e_mail': e_mail,}

        return HttpResponse(json.dumps({'order_data': order_data}), content_type='application/json')