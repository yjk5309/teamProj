from .common import *

def DeliveryCheckView(request):
    user = request.user
    idSql = "SELECT id FROM bookstore WHERE seller_id = (%s)"
    store_id = execute_and_get(idSql, (user,))
    productSql ="SELECT a.order_num, b.purchased_price, b.order_status, a.buy_date " \
                "FROM order_info as a JOIN order_products as b on a.order_num = b.order_num " \
                "WHERE b.store_id = (%s) and b.order_status = (%s) order by a.buy_date desc"
    delivery_datas = execute_and_get(productSql,(store_id[0][0],'결제 완료',))
    delivery_info = []
    for data in delivery_datas:
        row = {'order_num':data[0],
                   'purchased_price': data[1],
                   'order_status': data[2],
                   'buy_date': data[3],}
        delivery_info.append(row)
    return render(request, 'delivery_check.html', {'delivery_info': delivery_info})