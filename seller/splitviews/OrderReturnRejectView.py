from .common import *

def OrderReturnRejectView(request, return_id):
    reject_reason = request.POST.get('reject_reason')

    execute("UPDATE product_return SET reject_reason = (%s) WHERE id = (%s)", (reject_reason, return_id,))

    return redirect('seller:order_return')