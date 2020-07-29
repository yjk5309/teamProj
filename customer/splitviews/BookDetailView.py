from .common import *

def BookDetailView(request, book_id):
    book_datas = execute_and_get("SELECT book_name, author,  publisher, price, sales_status, inven, book_msg, book_img, isbn" +
                                " FROM book WHERE book_id = (%s)", (book_id,))

    book_store_name = execute_and_get("SELECT store_name FROM bookstore" +
                                      " LEFT OUTER JOIN book on book.store_id = bookstore.id WHERE book.book_id = (%s)", (book_id,))

    book = {'book_name': book_datas[0][0],
            'author': book_datas[0][1],
            'publisher': book_datas[0][2],
            'price': book_datas[0][3],
            'sales_status': book_datas[0][4],
            'inven': book_datas[0][5],
            'book_msg': book_datas[0][6],
            'book_img': book_datas[0][7],
            'isbn': book_datas[0][8],
            'store_name': book_store_name[0][0],}

    return render(request, "book_detail.html", {'book': book})