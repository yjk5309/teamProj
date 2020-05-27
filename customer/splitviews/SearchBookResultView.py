from .common import *

def SearchBookResultView(request):
    cursor = connection.cursor()

    title = request.POST.get('title')
    author = request.POST.get('author')
    publisher = request.POST.get('publisher')

    search_keyword = {'title': title,
                      'author': author,
                      'publisher': publisher,}

    search = "SELECT book_name, author, publisher, book_img, price"
    search += " FROM book"
    search += " WHERE book_name LIKE '%" + title + "%' AND author LIKE '%" + author + "%' AND publisher LIKE '%" + publisher + "%'"

    search_result = cursor.execute(search)
    search_datas = cursor.fetchall()

    search_list = []
    for search_data in search_datas:
        row = {'book_name': search_data[0],
               'author': search_data[1],
               'publisher': search_data[2],
               'book_img': search_data[3],
               'price': search_data[4],
            }
        search_list.append(row)

    connection.commit()
    connection.close()

    result = 1
    if len(search_list) == 0:
        result = 0

    return render(request, 'search_book_result.html', {'search_list':search_list, 'search_keyword':search_keyword,'result':result})