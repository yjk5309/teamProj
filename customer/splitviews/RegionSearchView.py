from .common import *

def RegionSearchView (request):
    if request.method == "POST":

        city = request.POST.get("city")
        province = request.POST.get('province')

        strSql = "SELECT store_name, address"
        strSql += " FROM bookstore"
        strSql += " WHERE address LIKE '" + province + "%" + city + "%'"

        try:
            cursor = connection.cursor()
            result = cursor.execute(strSql)
            citydata = cursor.fetchall()
            connection.commit()

        except:
            connection.rollback()

        if len(citydata) == 0:
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
                row = {'name': data[0], }
                provinces.append(row)

            return render(request, 'search_store.html', {'bookstores': bookstores,
                                                         'provinces': provinces})