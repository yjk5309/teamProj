from .common import *

def MainView(request):
    user = request.user

    store_manager = ''
    manager_data = execute_and_get("SELECT seller_id, id FROM bookstore WHERE seller_id = (%s)", (user.username,))

    if len(manager_data) != 0:
        store_manager = manager_data[0][0]

        product_count = execute_and_get("SELECT COUNT(*) FROM book_inven WHERE store_id = (%s)", (manager_data[0][1],))

        selling_info = {'product_count': product_count[0][0],
                        }

        return render(request, 'seller_main.html', {'store_manager': store_manager, 'selling_info':selling_info})

    else:
        return render(request, 'seller_main.html')