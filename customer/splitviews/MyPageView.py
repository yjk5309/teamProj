from .common import *

@login_required
def MyPageView(request):
    user = request.user

    like_bookSql = "SELECT a.book_isbn, b.book_name, b.book_img " \
                   "FROM like_list as a " \
                   "JOIN book as b " \
                   "ON a.book_isbn = b.isbn " \
                   "where a.user_id=(%s) ORDER BY date desc"

    datas = execute_and_get(like_bookSql,(user,))

    like_books = []
    for data in datas:
        row = {'isbn': data[0],
               'book_name': data[1],
               'book_img': data[2],
               }
        like_books.append(row)


    favorite_storeSql = "SELECT a.bookstore_id, b.store_name, b.bookstore_img " \
                        "FROM favorite_bookstore as a " \
                        "JOIN bookstore as b " \
                        "ON a.bookstore_id = b.id " \
                        "where a.user_id=(%s) ORDER BY date desc"

    datas = execute_and_get(favorite_storeSql,(user,))

    favorite_stores = []
    for data in datas:
        row = {'store_id': data[0],
               'store_name': data[1],
               'store_img': data[2],
               }
        favorite_stores.append(row)

    return render(request, 'mypage.html', {'like_books': like_books, 'favorite_stores': favorite_stores})