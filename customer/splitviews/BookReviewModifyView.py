from .common import *

def BookReviewModifyView(request, review_id):
    user = request.user

    current_review = execute_and_get('SELECT title, content FROM review WHERE user_id = (%s) AND id = (%s)',
                                     (user.username, review_id,))

    book_isbn = execute_and_get("SELECT book_isbn FROM review WHERE id = (%s)", (review_id,))
    store_id = execute_and_get("SELECT max(store_id) FROM book_inven WHERE book_isbn = (%s)", (book_isbn[0][0],))

    current_review_list = {
        'title': current_review[0][0],
        'content': current_review[0][1],
    }

    return redirect('customer:book_detail', book_isbn[0][0], store_id[0][0])