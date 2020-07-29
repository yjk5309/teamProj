from .common import *

@login_required
def BookLikeView(request, book_isbn):
    user = request.user

    is_like = execute_and_get("SELECT COUNT(*) FROM like_list WHERE user_id = (%s) AND book_isbn = (%s)",
                              (user.username, book_isbn,))

    if is_like[0][0] == 0:
        add_list = execute("INSERT INTO like_list(user_id, book_isbn) VALUES ((%s), (%s))",
                           (user.username, book_isbn,))

        like = 1

    elif is_like[0][0] == 1:
        delete_list = execute("DELETE FROM like_list WHERE user_id = (%s) AND book_isbn = (%s)",
                              (user.username, book_isbn,))

        like = 0

    return HttpResponse(json.dumps({'like': like}), content_type="application/json")