from .common import *

@login_required
def OrderDetailView(request,order_num):

    orderDetailSql = "SELECT a.order_num, b.first_name, a.order_name, a.order_address, " \
                     "a.order_p_num, a.order_memo, a.payment, sum(c.price) " \
                     "FROM order_info as a JOIN customer_accounts_user as b ON a.user_id = b.username " \
                     "JOIN order_products as c ON a.id = c.order_info_id where order_num = (%s)"

    data = execute_and_get(orderDetailSql,(order_num,))

    order_detail = {'order_num': data[0][0],
                    'user_name':data[0][1],
                    'order_name':data[0][2],
                    'order_address':data[0][3],
                    'order_p_num':data[0][4],
                    'order_memo':data[0][5],
                    'payment':data[0][6],
                    'price':data[0][7],
                    }

    return render(request, 'order_detail.html', {'order_detail':order_detail})