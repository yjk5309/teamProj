from .common import *

@login_required

def OrderConfirmView (request, order_info_id):

    uqdateSql = "UPDATE order_info SET order_num = id + 10000 + buy_date WHERE id = (%s)"
    execute(uqdateSql, (order_info_id,))

    order_num = execute_and_get("SELECT order_num FROM order_info where id = (%s)", (order_info_id,))

    if len(order_num) != 0:

        infoSql = "SELECT order_name, order_p_num, order_address, order_num " \
                  "FROM order_info where id = (%s)"

        data = execute_and_get(infoSql,(order_info_id,))

        info = {'order_name': data[0][0],
                'order_p_num': data[0][1],
                'order_address': data[0][2],
                'order_num':data[0][3],
                 }

    productSql = "SELECT a.book_name, c.store_name, a.price, a.book_img " \
                 "FROM book AS a " \
                 "JOIN order_products AS b " \
                 "ON a.isbn = b.isbn " \
                 "JOIN bookstore AS c " \
                 "ON b.store_id = c.id " \
                 "where order_info_id = (%s)"

    datas = execute_and_get(productSql,(order_info_id,))

    products = []
    for data in datas:
        row = {
            'book_name':data[0],
            'store_name':data[1],
            'price':data[2],
            'book_img':data[3],
            }
        products.append(row)

    paymentSql = "SELECT payment, date_add(buy_date,INTERVAL 1 DAY) FROM order_info where id = (%s)"

    data = execute_and_get(paymentSql, (order_info_id,))
    payment = {'payment': data[0][0],
               'due_date': data[0][1],
               }

    accountSql = "SELECT c.store_name, sum(a.price), b.account, b.bank " \
                 "FROM order_products AS a " \
                 "JOIN shipping_info AS b ON a.store_id = b.bookstore_id " \
                 "JOIN bookstore AS c ON a.store_id = c.id " \
                 "WHERE order_info_id = (%s) GROUP BY store_id"

    account_datas = execute_and_get(accountSql, (order_info_id,))

    account_info = []
    for data in account_datas:
        row = {
            'store_name':data[0],
            'price':data[1],
            'account':data[2],
            'bank':data[3],
            }
        account_info.append(row)

    return render(request, 'order_confirm.html', {'info': info, 'products':products,
                                                  'payment':payment, 'account_info':account_info})