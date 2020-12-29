from .common import *

@login_required
def OrderCancelView(request, order_num):
    execute("UPDATE order_products SET order_status = '결제취소' WHERE order_num = (%s) AND " +
            "order_status = (%s) OR order_status = (%s)", (order_num, '결제 대기중', '결제 완료',))

    return redirect("customer:mypage")