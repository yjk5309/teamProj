from .common import *
import pyautogui

@login_required
def BookBasketInsertView(request, book_isbn, store_id):
    if 'user_basket' not in request.session:
        request.session['user_basket'] = []

    tab = 'basket'

    book_info = execute_and_get("SELECT book_name, book_img, price, publisher, isbn FROM book WHERE isbn = (%s)", (book_isbn,))
    store_name = execute_and_get("SELECT store_name FROM bookstore WHERE id = (%s)", (store_id,))

    for i in range(len(request.session['user_basket'])):
        if request.session['user_basket'][i]['isbn'] == book_isbn and request.session['user_basket'][i]['store_name'] == store_id:
            del request.session['user_basket'][i]

    book = {'book_name': book_info[0][0],
          'book_img': book_info[0][1],
          'price': book_info[0][2],
          'publisher': book_info[0][3],
          'isbn':book_info[0][4],
          'store_name': store_name[0][0],
          'store_id': store_id
              }

    request.session['user_basket'].append(book)
    request.session.modified = True

    return render(request, 'mypage.html', {'tab': tab})