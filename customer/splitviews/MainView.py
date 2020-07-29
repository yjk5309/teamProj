from .common import *

def MainView (request):

    bookSql = "SELECT book_name, book_img, book_id FROM book order by inven limit 3"

    storeSql = "SELECT store_name, store_msg FROM bookstore limit 3"

    datas = execute_and_get(bookSql)

    datas2 = execute_and_get(storeSql)

    books = []
    for data in datas:
        row = {'book_name':data[0],
               'book_img':data[1],
               'book_id':data[2],
               }
        books.append(row)

    stores = []
    for data in datas2:
        row = {'store_name': data[0],
               'store_msg': data[1]
               }
        stores.append(row)

    return render(request, 'main.html',{'books':books, 'stores':stores})