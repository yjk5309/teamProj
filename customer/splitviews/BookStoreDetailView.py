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

    favoriteSql = "SELECT EXISTS (SELECT id FROM favorite_bookstore WHERE bookstore_id=(%s) AND user_id=(%s))"

    favorite_data = execute_and_get(favoriteSql, (store_id,user.username,))

    is_favorite = favorite_data[0][0]

    bookSql =  "SELECT a.isbn, a.book_name, a.price, a.book_img, b.store_id " \
               "FROM book AS a " \
               "JOIN book_inven AS b " \
               "ON a.isbn = b.book_isbn " \
               "where store_id = (%s)"

    datas = execute_and_get(bookSql,(store_id,))

    books = []
    for data in datas:
        row = {
            'isbn':data[0],
            'book_name':data[1],
            'price':data[2],
            'book_img':data[3],
            'store_id':data[4],
            }
        books.append(row)

    return render(request, 'bookstore_detail.html',{'store':store, 'is_favorite':is_favorite, 'books':books})