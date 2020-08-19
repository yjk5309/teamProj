from .common import *
import pyautogui

@login_required
def BookBasketInsertView(request, book_isbn):
    if 'test' not in request.session:
        request.session['test'] = []

    tab = 'basket'

    book_info = execute_and_get("SELECT book_name, book_img, price, publisher, isbn FROM book WHERE isbn = (%s)", (book_isbn,))

    for i in range(len(request.session['test'])):
        if request.session['test'][i]['isbn'] == book_isbn:
            del request.session['test'][i]

    ts = {'book_name': book_info[0][0],
          'book_img': book_info[0][1],
          'price': book_info[0][2],
          'publisher': book_info[0][3],
          'isbn':book_info[0][4]
              }

    request.session['test'].append(ts)
    request.session.modified = True

    return render(request, 'mypage.html', {'tab': tab})