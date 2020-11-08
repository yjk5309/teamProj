from .common import *

def OrderDecisionView(request, order_num):

    order_status = execute_and_get("SELECT order_status FROM order_products WHERE order_num = (%s)", (order_num,))

    if order_status[0][0] == "배송 완료":
        execute("UPDATE order_products SET order_status = '구매확정' WHERE order_num = (%s)", (order_num,))

    return redirect("customer:mypage")