from .common import *

def OrderCreateView (request):
    user = request.user
    if request.method == 'GET':
        isbn = request.GET.get('isbn')
        store_name = request.GET.get('store_name')

        storeIdSql = "SELECT id FROM bookstore where store_name=(%s)"
        store_id = execute_and_get(storeIdSql,(store_name,))

        bookSql = "SELECT a.book_name, a.price, a.book_img " \
                  "FROM book AS a " \
                  "JOIN book_inven AS b " \
                  "ON a.isbn = b.book_isbn " \
                  "where a.isbn = (%s) and b.store_id = (%s)"

        data = execute_and_get(bookSql, (isbn, store_id,))

        goods = {'book_name': data[0][0],
                 'price': data[0][1],
                 'book_img': data[0][2],
                 'store_name':store_name,
                 }

        return render(request, 'order_sheet.html',{'goods':goods})

    else:
        name = request.POST.get('name')
        e_mail = request.POST.get('e_mail')
        phone_number = request.POST.get('p_number')
        address = request.POST.get('address')

        user.first_name = name
        user.email = e_mail
        user.phone_number = phone_number
        user.address = address

        user.save()

        isbn = request.GET.get('isbn')
        store_name = request.GET.get('store_name')

        storeIdSql = "SELECT id FROM bookstore where store_name=(%s)"
        store_id = execute_and_get(storeIdSql, (store_name,))

        bookSql = "SELECT a.book_name, a.price, a.book_img " \
                  "FROM book AS a " \
                  "JOIN book_inven AS b " \
                  "ON a.isbn = b.book_isbn " \
                  "where a.isbn = (%s) and b.store_id = (%s)"

        data = execute_and_get(bookSql, (isbn, store_id,))

        goods = {'book_name': data[0][0],
                 'price': data[0][1],
                 'book_img': data[0][2],
                 'store_name': store_name,
                 }

        return render(request, 'order_sheet.html',{'goods':goods})