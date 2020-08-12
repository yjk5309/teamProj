from .common import *

def BookReviewModifyView(request, review_id):
    user = request.user

    current_review = execute_and_get('SELECT title, content FROM review WHERE user_id = (%s) AND id = (%s)',
                                     (user.username, review_id,))

    current_review_list = {
        'title': current_review[0][0],
        'content': current_review[0][1],
    }

    return redirect('customer:book_review_modify', review_id)