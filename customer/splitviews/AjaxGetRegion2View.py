from .common import *

@require_POST
def AjaxGetRegion2View(request):

    region1_name = request.POST.get('region1_name')

    strSql = "SELECT region2"
    strSql += " FROM region2"
    strSql += " JOIN region1 ON region1.id = region2.region1_id"
    strSql += " WHERE region1 = (%s)"

    try:
        cursor = connection.cursor()
        result = cursor.execute(strSql, (region1_name,))
        datas = cursor.fetchall()
        connection.commit()

    except:
        connection.rollback()

    region2s = []
    for data in datas:
        raw_dict = {
            "name": data[0],
        }

        region2s.append(raw_dict)

    return HttpResponse(json.dumps({'region2s': region2s}), content_type="application/json")
