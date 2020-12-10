from .common import *

@login_required
def ReviewManageView(request):
    user = request.user
    id_sql = "SELECT id FROM bookstore WHERE seller_id = (%s)"
    store_id = execute_and_get(id_sql, (user,))

    lately_review_sql = "SELECT user_id, title, content, evaluate_score, id, date " \
                        "FROM review WHERE store_id= (%s) ORDER BY date DESC"
    datas = execute_and_get(lately_review_sql, (store_id[0][0],))
    lately_review = []
    for data in datas:
        row = {'user_id': data[0],
               'title': data[1],
               'content': data[2],
               'evaluate_score': data[3],
               'id': data[4],
               'date': data[5],
               }
        lately_review.append(row)
    return render(request, 'review_manage.html', {'lately_review': lately_review})