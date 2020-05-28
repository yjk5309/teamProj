from .common import *

def SearchStoreView (request):
    strSql = "SELECT store_name, address FROM bookstore"

    try:
        cursor = connection.cursor()
        result = cursor.execute(strSql)
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

    import json
    bookstores = json.dumps(bookstores)
    return render(request, 'search_store.html', context={'bookstores': bookstores})