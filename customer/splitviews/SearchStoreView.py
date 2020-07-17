from .common import *

def SearchStoreView (request):
    if request.method == "GET":
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
            json_row = json.dumps(row)
            bookstores.append(json_row)
        bookstores = json.dumps(bookstores)


        strSql = "SELECT province FROM province"

        try:
            cursor = connection.cursor()
            result = cursor.execute(strSql)
            datas = cursor.fetchall()
            connection.commit()

        except:
            connection.rollback()

        provinces = []
        for data in datas:
            row = {'name': data[0],}
            provinces.append(row)

        return render(request, 'search_store.html', {'bookstores': bookstores,
                                                     'provinces': provinces})