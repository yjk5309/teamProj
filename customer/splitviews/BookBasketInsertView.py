from .common import *
import pyautogui

@login_required
def BookBasketInsertView(request, book_isbn):
    user = request.user
    tab = 'basket'

    book_info = execute_and_get("SELECT book_name, book_img, price, publisher, isbn FROM book WHERE isbn = (%s)", (book_isbn,))

    request.session['user_id'] = user.username
    request.session['book_name'] = book_info[0][0]
    request.session['book_img'] = book_info[0][1]
    request.session['price'] = book_info[0][2]
    request.session['publisher'] = book_info[0][3]
    request.session['isbn'] = book_info[0][4]

    basket = book_basket

    basket_data = {
        'book_name': request.session['book_name'],
        'book_img': request.session['book_img'],
        'price': request.session['price'],
        'user_id': request.session['user_id'],
        'publisher': request.session['publisher'],
        'isbn':request.session['isbn'],
              }
    basket.append(basket_data)

    pyautogui.alert(text='장바구니에 추가되었습니다.', title='알림')

    return render(request, 'mypage.html', {'basket': basket, 'tab':tab})