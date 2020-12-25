from .common import *

@login_required
def OrderCancelView(request, order_num):
    order_status = execute_and_get("SELECT order_status FROM order_products WHERE order_num = (%s)", (order_num,))

    execute("UPDATE order_products SET order_status = '결제취소' " +
            "WHERE order_num = (%s) AND order_status = (%s)", (order_num, order_status[0][0],))

    return redirect("customer:mypage")