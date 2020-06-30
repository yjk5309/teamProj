from .common import *

def MainView (request):

    bookSql = "SELECT book_name, book_img, book_id FROM book order by inven limit 3"

    storeSql = "SELECT store_name, store_msg FROM omp2.bookstore limit 3"

    try:
        cursor = connection.cursor()
        result = cursor.execute(bookSql,)
        datas = cursor.fetchall()

        result2 = cursor.execute(storeSql, )
        datas2 = cursor.fetchall()

        connection.commit()

    except:
        connection.rollback()

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

    return render(request, 'main.html',{'books':books, 'stores':stores })