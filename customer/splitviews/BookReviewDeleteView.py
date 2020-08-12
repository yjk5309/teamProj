from .common import *

@login_required
def BookReviewDeleteView(request, review_id):
    user = request.user

    book_isbn = execute_and_get("SELECT book_isbn FROM review WHERE id = (%s)", (review_id,))

    execute("DELETE FROM review WHERE user_id = (%s) AND id = (%s)", (user.username, review_id,))

    return redirect('customer:book_detail', book_isbn[0][0])