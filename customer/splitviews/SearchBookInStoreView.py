from .common import *

def SearchBookInStoreView (request, store_id):
    tab = 'search_book'

    search_book = request.POST.get('search_book')

    bookSql = "SELECT a.book_isbn, a.book_name, a.price, b.book_img, a.store_id " \
              "FROM book_inven as a JOIN book as b on a.book_isbn = b.isbn " \
              "WHERE a.store_id = (%s) and (a.book_name LIKE '%" + search_book + "%' or b.author LIKE '%" + search_book + "%') GROUP BY a.book_name"

    datas = execute_and_get(bookSql, (store_id,))

    books = []
    for data in datas:
        row = {
            'isbn':data[0],
            'book_name':data[1],
            'price':data[2],
            'book_img':data[3],
            'store_id':data[4],
            }
        books.append(row)

    if search_book == "":
        messages.error(request, '검색 키워드를 하나 이상 입력해주세요.')
        return redirect('customer:bookstore_detail', store_id)

    return render(request, 'bookstore_detail.html',{'tab':tab,'books':books,'search_book':search_book})