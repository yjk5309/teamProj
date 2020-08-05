from .common import *

@require_POST
def AjaxGetSubCategoryView(request):

    main_name = request.POST.get('main_name')

    strSql = "SELECT sub_category FROM omp3.sub_category " \
             "JOIN main_category ON sub_category.main_category_id = main_category.id " \
             "WHERE main_category = (%s) and origin = '국내도서'"

    datas = execute_and_get(strSql, (main_name,))

    subs = []
    for data in datas:
        raw_dict = {
            "name": data[0],
        }

        subs.append(raw_dict)

    return HttpResponse(json.dumps({'subs': subs}), content_type="application/json")
