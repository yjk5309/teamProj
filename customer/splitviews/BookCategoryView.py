from .common import *

def BookCategoryView (request):
    strSql = "SELECT main_category FROM main_category WHERE origin ='국내도서'"

    datas = execute_and_get(strSql)

    mains = []
    for data in datas:
        row = {'name': data[0], }
        mains.append(row)

    return render(request, 'domestic_book.html', {'mains': mains})