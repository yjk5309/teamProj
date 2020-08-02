from .common import *

@login_required
def BookLikeView(request, book_isbn):
    user = request.user

    is_like = execute_and_get("SELECT IF (user_id = (%s) AND book_isbn = (%s), true, false) as result from like_list",
                              (user.username, book_isbn,))

    if (1,) not in is_like:
        add_list = execute("INSERT INTO like_list(user_id, book_isbn) VALUES ((%s), (%s))",
                           (user.username, book_isbn,))

        like = 1

    else:
        delete_list = execute("DELETE FROM like_list WHERE user_id = (%s) AND book_isbn = (%s)",
                              (user.username, book_isbn,))

        like = 0

    return HttpResponse(json.dumps({'like': like}), content_type="application/json")