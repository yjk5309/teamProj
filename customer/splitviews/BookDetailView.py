from .common import *

def BookDetailView(request, book_isbn):
    user = request.user
    book_datas = execute_and_get("SELECT book_name, author,  publisher, price, book_msg, book_img, isbn" +
                                " FROM book WHERE isbn = (%s)", (book_isbn,))

    current_book_store_name = execute_and_get("SELECT store_name FROM bookstore" +
                                      " LEFT OUTER JOIN book_inven on book_inven.store_id = bookstore.id WHERE book_inven.book_isbn = (%s)", (book_isbn,))

    is_like = execute_and_get("SELECT EXISTS(SELECT * FROM like_list WHERE user_id = (%s) AND book_isbn = (%s))",
                              (user.username, book_isbn,))

    book_inven = execute_and_get("SELECT CONVERT(SUM(inven), signed integer) FROM book_inven  WHERE book_name = (%s)", (book_datas[0][0],))

    book_review_datas = execute_and_get("SELECT ROUND(AVG(evaluate_score),1), COUNT(book_name), user_id, title, content, evaluate_score" +
                                   " FROM review WHERE book_name= (%s)",
                                   (book_datas[0][0],))

    review_list = execute_and_get("SELECT user_id, title, content, evaluate_score, id FROM review WHERE book_name= (%s) ORDER BY CAST(evaluate_score AS signed integer) DESC",
                        (book_datas[0][0],))

    book = {'book_name': book_datas[0][0],
            'author': book_datas[0][1],
            'publisher': book_datas[0][2],
            'price': book_datas[0][3],
            'book_msg': book_datas[0][4],
            'book_img': book_datas[0][5],
            'isbn': book_datas[0][6],
            'store_name': current_book_store_name[0][0],
            'book_inven': book_inven[0][0],
            'review_score': book_review_datas[0][0],
            'review_count': book_review_datas[0][1],
            }

    review = []
    for review_data in review_list:
        review_row = {
            'user_id': review_data[0],
            'title': review_data[1],
            'content': review_data[2],
            'evaluate_score': review_data[3],
            'id': review_data[4],
        }
        review.append(review_row)

    sale_stores = execute_and_get("SELECT store_name, book_isbn, CONVERT(SUM(inven), signed integer) FROM bookstore" +
                                  " LEFT OUTER JOIN book_inven on book_inven.store_id = bookstore.id WHERE book_inven.book_name = (%s)  GROUP BY store_name"
                                  , (book_datas[0][0],))

    sale_stores_list = []
    for sale_store in sale_stores:
        each_book_price = execute_and_get("SELECT price FROM book " +
                                          "LEFT OUTER JOIN book_inven on book_inven.book_isbn = book.isbn WHERE book.isbn = (%s)"
                                          , (sale_store[1],))
        row = {'store_name': sale_store[0],
               'isbn': sale_store[1],
               'inven': sale_store[2],
               'price': each_book_price[0][0],
            }

        sale_stores_list.append(row)

    return render(request, "book_detail.html", {'book': book, 'is_like': is_like[0][0], 'review': review,
                                                'sale_stores_list': sale_stores_list})