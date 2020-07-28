from .common import *

def BookStoreDetailView (request, store_id):

    storeSql = "SELECT store_name, address, phone_num, bookstore_img, store_msg FROM bookstore where id =(%s)"

    data = excute_and_get(storeSql,(store_id,))

    store = {'store_name': data[0][0],
             'address': data[0][1],
             'phone_num': data[0][2],
             'bookstore_img': data[0][3],
             'store_msg': data[0][4],
            }

    return render(request, 'bookstore_detail.html',{'store':store})