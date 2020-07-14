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

    elif request.method == "POST":
        keyword = request.POST.get("search_store")
        city = request.POST.get("city")

        if keyword is None:

            strSql = "SELECT store_name, address"
            strSql += " FROM bookstore"
            strSql += " WHERE address LIKE '%" + city + "%'"

            try:
                cursor = connection.cursor()
                result = cursor.execute(strSql)
                citydata = cursor.fetchall()
                connection.commit()

            except:
                connection.rollback()

            if len(citydata)== 0:
                messages.error(request, '해당지역에 등록된 서점이 없습니다.')
                return redirect('customer:search_store')

            else:

                bookstores = []
                for data in citydata:
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

        else :
            nameSql = "SELECT store_name, address"
            nameSql += " FROM bookstore"
            nameSql += " WHERE store_name LIKE '%" + keyword + "%'"

            try:
                cursor = connection.cursor()
                result = cursor.execute(nameSql)
                namedata = cursor.fetchall()
                connection.commit()

            except:
                connection.rollback()

            if len(namedata)==0 :
                messages.error(request, '아직 등록되지 않은 서점입니다.')
                return redirect('customer:search_store')

            else:

                bookstores = []
                for data in namedata:
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
                    row = {'name': data[0], }
                    provinces.append(row)

                return render(request, 'search_store.html', {'bookstores': bookstores,
                                                             'provinces': provinces})
