from .common import *

def KeywordSearchView (request):
    if request.method == "POST":
        keyword = request.POST.get("search_store")

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

        if len(namedata) == 0:
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
