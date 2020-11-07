from .common import *

def OrderDetailView(request, order_num):
    user = request.user

    order_product = execute_and_get("SELECT isbn, quantity FROM order_products WHERE order_num = (%s)", (order_num,))

    order_info = execute_and_get("SELECT order_name, order_address, order_p_num, order_email, order_memo " +
                                 "FROM order_info WHERE order_num = (%s)", (order_num,))

    book_info = execute_and_get("SELECT book_name, author, publisher, book_img FROM book WHERE isbn = (%s)", (order_product[0][0],))

    order_detail = {'isbn': order_product[0][0],
                    'quantity': order_product[0][1],
                    'order_name': order_info[0][0],
                    'order_address': order_info[0][1],
                    'order_p_num': order_info[0][2],
                    'order_email': order_info[0][3],
                    'order_memo': order_info[0][4],
                    'book_name': book_info[0][0],
                    'author': book_info[0][1],
                    'publisher': book_info[0][2],
                    'book_img': book_info[0][3],}

    return HttpResponse(json.dumps({'order_detail': order_detail}), content_type="application/json")