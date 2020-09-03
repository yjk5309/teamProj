from .common import *

def OrderSheetCartView (request):
    if request.method == 'POST':
        tab = 'basket'
        checked_cart = request.POST.getlist('cart')
        bookSql = "SELECT a.book_name, a.price, a.book_img, c.store_name " \
                  "FROM book AS a " \
                  "JOIN book_inven AS b " \
                  "ON a.isbn = b.book_isbn " \
                  "JOIN bookstore AS c " \
                  "ON b.store_id = c.id " \
                  "where a.isbn = (%s) and b.store_id = (%s)"
        cart_list = []
        for cart in checked_cart:
            cart = cart.split(",")
            store_id = cart[0]
            isbn = cart[1]
            row = {'isbn': isbn,
                   'store_id': store_id,
                   }
            cart_list.append(row)

        datas = []
        for book in cart_list:
            datas.append(execute_and_get(bookSql, (book['isbn'], book['store_id'],)))

        carts = []
        for data in datas:
            row = {'book_name': data[0][0],
                    'price': data[0][1],
                    'book_img': data[0][2],
                    'store_name': data[0][3],
                    }
            carts.append(row)

    return render(request,'order_sheet.html',{'carts':carts,'tab': tab})