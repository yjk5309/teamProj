from .common import *

def BookDetailView(request, book_isbn):
    user = request.user
    book_datas = execute_and_get("SELECT book_name, author,  publisher, price, book_msg, book_img, isbn" +
                                " FROM book WHERE isbn = (%s)", (book_isbn,))

    book_store_name = execute_and_get("SELECT store_name FROM bookstore" +
                                      " LEFT OUTER JOIN book_inven on book_inven.store_id = bookstore.id WHERE book_inven.book_isbn = (%s)", (book_isbn,))

    is_like = execute_and_get("SELECT IF (user_id = (%s) AND book_isbn = (%s), true, false) as result from like_list",
                              (user.username, book_isbn,))

    book_inven = execute_and_get("SELECT COUNT(*) FROM book_inven  WHERE book_name = (%s)", (book_datas[0][0],))

    if (1,) not in is_like:
        like = 1
    else:
        like = 0

    book = {'book_name': book_datas[0][0],
            'author': book_datas[0][1],
            'publisher': book_datas[0][2],
            'price': book_datas[0][3],
            'book_msg': book_datas[0][4],
            'book_img': book_datas[0][5],
            'isbn': book_datas[0][6],
            'store_name': book_store_name[0][0],
            'book_inven': book_inven[0][0]}

    return render(request, "book_detail.html", {'book': book, 'like': like})