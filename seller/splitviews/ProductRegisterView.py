from .common import *

def ProductRegisterView(request):
    if request.method == 'GET':
        return render(request, 'product_register.html')

    elif request.method == 'POST':
        user = request.user

        book_name = request.POST.get('book_name')
        book_isbn = request.POST.get('book_isbn')
        inven = request.POST.get('inven')
        price = request.POST.get('price')

        store_id = execute_and_get("SELECT id FROM bookstore WHERE seller_id = (%s)", (user.username,))

        execute("INSERT INTO book_inven(book_isbn, book_name, store_id, inven, price) "+
                "VALUES ((%s), (%s), (%s), (%s), (%s))", (book_isbn, book_name, store_id[0][0], inven, price))

        return redirect('seller:main')




