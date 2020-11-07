from .common import *

def OrderCheckView(request):
    user = request.user

    seller_id = execute_and_get("SELECT id FROM bookstore WHERE seller_id=(%s)", (user.username,))

    order_data = execute_and_get("SELECT order_num, purchased_price, order_status FROM order_products WHERE store_id = (%s)",
                                 (seller_id[0][0],))

    order_info_list = []
    for order_datas in order_data:
        buyer_data = execute_and_get("SELECT payment, buy_date FROM order_info WHERE order_num = (%s)", (order_datas[0],))
        if order_datas[2] == "결제 대기중":
            row = {'order_num': order_datas[0],
                   'purchased_price': order_datas[1],
                   'order_status': order_datas[2],
                   'buy_date': buyer_data[0][1],
                   'payment': buyer_data[0][0]}

            order_info_list.append(row)

    return render(request, 'order_check.html', {'order_info_list': order_info_list})