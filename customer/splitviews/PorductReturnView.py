from .common import *

def ProductReturnView(request, order_id):
    if request.method == "GET":
        product_info = execute_and_get("SELECT store_id , isbn, purchased_price FROM order_products WHERE id = (%s)", (order_id,))

        book_name = execute_and_get("SELECT book_name FROM book WHERE isbn = (%s)", (product_info[0][1],))
        store_name = execute_and_get("SELECT store_name FROM bookstore WHERE id = (%s)", (product_info[0][0],))

        order_info = {'book_name': book_name[0][0],
                      'price': product_info[0][2],
                      'bookstore': store_name[0][0]}

        return render(request, 'product_return.html', {'order_id': order_id, 'order_info': order_info})

    elif request.method == "POST":

        return redirect('customer:mypage')