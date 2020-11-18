from .common import *

def SettlementCheckView(request):
    user = request.user
    id_sql = "SELECT id FROM bookstore WHERE seller_id = (%s)"
    store_id = execute_and_get(id_sql, (user,))
    if request.method == 'GET':
        product_sql = "SELECT a.order_num, b.purchased_price, a.buy_date, " \
                      "CASE is_settlement_confirm WHEN False THEN '정산 대기' WHEN True THEN '정산 완료' ELSE '구매 확정' END AS settlement_status " \
                      "FROM order_info as a JOIN order_products as b on a.order_num = b.order_num " \
                      "WHERE b.store_id = (%s) and b.order_status = (%s) " \
                      "order by a.buy_date desc"
        datas = execute_and_get(product_sql, (store_id[0][0], '구매 확정',))
        settlement_info = []
        for data in datas:
            row = {'order_num': data[0],
                   'purchased_price': data[1],
                   'buy_date': data[2],
                   'settlement_status': data[3], }
            settlement_info.append(row)
        return render(request, 'settlement_check.html', {'settlement_info': settlement_info})

    else:
        settlement_status = request.POST.get('settlement_status')
        if len(settlement_status) == 0:
            product_sql = "SELECT a.order_num, b.purchased_price, a.buy_date, " \
                          "CASE is_settlement_confirm WHEN False THEN '정산 대기' WHEN True THEN '정산 완료' ELSE '구매 확정' END AS settlement_status " \
                          "FROM order_info as a JOIN order_products as b on a.order_num = b.order_num " \
                          "WHERE b.store_id = (%s) and b.order_status = (%s) " \
                          "order by a.buy_date desc"

        else:
            product_sql = "SELECT a.order_num, b.purchased_price, a.buy_date, " \
                          "CASE is_settlement_confirm WHEN False THEN '정산 대기' WHEN True THEN '정산 완료' ELSE '구매 확정' END AS settlement_status " \
                          "FROM order_info as a JOIN order_products as b on a.order_num = b.order_num " \
                          "WHERE b.store_id = (%s) and b.order_status = (%s) and b.is_settlement_confirm is " + settlement_status + " " \
                          "order by a.buy_date desc"
        datas = execute_and_get(product_sql, (store_id[0][0], '구매 확정',))
        settlement_info = []
        for data in datas:
            row = {'order_num': data[0],
                   'purchased_price': data[1],
                   'buy_date': data[2],
                   'settlement_status': data[3], }
            settlement_info.append(row)
        return render(request, 'settlement_check.html', {'settlement_info': settlement_info})