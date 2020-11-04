from .common import *

def PayCheckAjaxView(request, order_num):
    user = request.user

    order_status = execute_and_get("SELECT order_status FROM order_products WHERE order_num = (%s)", (order_num,))

    if order_status[0][0] == "결제 대기중":
        execute("UPDATE order_products SET order_status = '결제 완료' WHERE order_num = (%s)", (order_num,))
    else:
        execute("UPDATE order_products SET order_status = '결제 대기중' WHERE order_num = (%s)", (order_num,))

    update_order_status = execute_and_get("SELECT order_status FROM order_products WHERE order_num = (%s)", (order_num,))

    return HttpResponse(json.dumps({'update_order_status': update_order_status[0][0]}), content_type="application/json")