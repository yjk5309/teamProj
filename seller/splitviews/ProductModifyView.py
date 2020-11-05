from .common import *

@login_required
def ProductModifyView(request):

    return render(request,'product_modify.html')