from .common import *

def OrderCreateView (request, book_isbn, store_id):

    if request.method == 'GET':

        bookSql = "SELECT a.book_name, a.price, a.book_img, c.store_name " \
                  "FROM book AS a " \
                  "JOIN book_inven AS b " \
                  "ON a.isbn = b.book_isbn " \
                  "JOIN bookstore AS c " \
                  "ON b.store_id = c.id " \
                  "where a.isbn = (%s) and b.store_id = (%s)"

        data = execute_and_get(bookSql, (book_isbn, store_id,))

        goods = {'book_name': data[0][0],
                 'price': data[0][1],
                 'book_img': data[0][2],
                 'store_name':data[0][3],
                 }

        return render(request, 'order_sheet.html',{'goods':goods})