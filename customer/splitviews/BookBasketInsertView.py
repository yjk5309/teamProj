from .common import *

@login_required
def BookBasketInsertView(request, book_isbn):
    user = request.user

    book_info = execute_and_get("SELECT book_name, book_img, price FROM book WHERE isbn = (%s)", (book_isbn,))

    request.session['user_id'] = user.username
    request.session['book_name'] = book_info[0][0]
    request.session['book_img'] = book_info[0][1]
    request.session['price'] = book_info[0][2]

    basket = {'book_name': request.session['book_name'],
              'book_img': request.session['book_img'],
              'price': request.session['price'],
              'user_id': request.session['user_id']
              }

    return render(request, 'mypage.html', {'basket': basket})