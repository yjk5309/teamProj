from .common import *

def SearchStoreView (request):
    strSql = "SELECT store_name, address FROM bookstore"

    try:
        cursor = connection.cursor()
        result = cursor.execute(strSql, (request,))
        storedata = cursor.fetchall()
        connection.commit()

    except:
        connection.rollback()

    bookstores = []
    for data in storedata:
        row = {'store_name': data[0],
               'address': data[1],
               }
        bookstores.append(row)

    return HttpResponse(json.dumps({'bookstores': bookstores}), content_type="application/json")