from .common import *

@login_required
def ProductModifyView(request):
    store_id = request.POST.get('store_id')
    isbn = request.POST.get('isbn')
    book_sql = "SELECT book_name, inven, price, book_msg " \
               "FROM book_inven WHERE store_id=(%s) and book_isbn=(%s) "
    data = execute_and_get(book_sql, (store_id, isbn,))


    return render(request, 'product_modify.html', {})