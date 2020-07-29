from .common import *

def BookStoreDetailView (request, store_id):
    user = request.user

    storeSql = "SELECT store_name, address, phone_num, bookstore_img, store_msg, id FROM bookstore where id =(%s)"

    data = execute_and_get(storeSql,(store_id,))

    store = {'store_name': data[0][0],
             'address': data[0][1],
             'phone_num': data[0][2],
             'store_img': data[0][3],
             'store_msg': data[0][4],
             'store_id':data[0][5],
            }

    favoriteSql = "SELECT count(*) FROM favorite_bookstore WHERE bookstore_id=(%s) AND user_id=(%s)"

    favorite_data = execute_and_get(favoriteSql, (store_id,user.username,))

    favorite = favorite_data[0][0]

    return render(request, 'bookstore_detail.html',{'store':store, 'favorite':favorite})