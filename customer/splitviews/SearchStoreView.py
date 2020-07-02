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


        strSql = "SELECT region1 FROM region1"

        try:
            cursor = connection.cursor()
            result = cursor.execute(strSql)
            datas = cursor.fetchall()
            connection.commit()

        except:
            connection.rollback()

        region1s = []
        for data in datas:
            row = {'name': data[0],}
            region1s.append(row)

        return render(request, 'search_store.html', {'bookstores': bookstores,
                                                     'region1s': region1s})

    elif request.method == "POST":
        keyword = request.POST.get("search_store")

        strSql = "SELECT store_name, address"
        strSql += " FROM bookstore"
        strSql += " WHERE store_name LIKE '%" + keyword + "%'"

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


        strSql = "SELECT region1 FROM region1"

        try:
            cursor = connection.cursor()
            result = cursor.execute(strSql)
            datas = cursor.fetchall()
            connection.commit()

        except:
            connection.rollback()

        region1s = []
        for data in datas:
            row = {'name': data[0],}
            region1s.append(row)

        return render(request, 'search_store.html', {'bookstores': bookstores,
                                                     'region1s': region1s})