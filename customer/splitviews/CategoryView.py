from .common import *

def CategoryView (request):
    strSql = "SELECT id, main_category FROM main_category WHERE origin ='국내도서'"

    datas = execute_and_get(strSql)

    domestic = []
    for data in datas:
        row = {
            'main_category_id': data[0],
            'main_category':data[1],
        }
        domestic.append(row)

    strSql = "SELECT id, main_category FROM main_category WHERE origin ='외국도서'"

    datas = execute_and_get(strSql)

    foreign = []
    for data in datas:
        row = {
            'main_category_id': data[0],
            'main_category':data[1],
        }
        foreign.append(row)

    bookSql =  "SELECT isbn, book_name, price, book_img FROM book "

    datas = execute_and_get(bookSql)

    books = []
    for data in datas:
        row = {
            'isbn':data[0],
            'book_name':data[1],
            'price':data[2],
            'book_img':data[3],
            }
        books.append(row)

    return render(request, 'category.html', {'domestic':domestic,'foreign': foreign,'books':books})