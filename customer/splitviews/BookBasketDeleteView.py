from .common import *

def BookBasketDeleteView(request, book_isbn):
    tab = 'basket'

    book_info = execute_and_get("SELECT book_name, book_img, price, publisher, isbn FROM book WHERE isbn = (%s)",
                                (book_isbn,))

    for i in range(len(request.session['test'])):
        if request.session['test'][i]['isbn'] == book_isbn:
            del request.session['test'][i]
            break

    request.session.modified = True

    return render(request, 'mypage.html', {'tab': tab})