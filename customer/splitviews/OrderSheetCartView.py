from .common import *

def OrderSheetCartView (request):
    if request.method == 'POST':
        tab = 'basket'
        checked_cart = request.POST.getlist('cart')
        bookSql = "SELECT a.book_name, b.price, a.book_img, c.store_name " \
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
            quantity = cart[2]
            row = {'isbn': isbn,
                   'store_id': store_id,
                   'quantity': quantity,
                   }
            cart_list.append(row)

        datas = []
        for book in cart_list:
            datas.append(execute_and_get(bookSql, (book['isbn'], book['store_id'],)))

        carts = []
        total_price = 0
        for data in datas:
            row = {'book_name': data[0][0],
                    'price': data[0][1],
                    'book_img': data[0][2],
                    'store_name': data[0][3],
                   }
            carts.append(row)

        quantity_datas = []
        for book in cart_list:
            quantity_datas.append(book['quantity'])

        quantity = []
        for quantity_data in quantity_datas:
            row = {'quantity': quantity_data[0][0],
                   }
            quantity.append(row)
            total_price += data[0][1]*int(quantity_data[0][0])

    return render(request,'order_sheet.html',{'carts':carts,'quantity':quantity,
                                              'tab': tab, 'total_price': total_price})