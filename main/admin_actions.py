from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect

from main import services

ALLOWED_EXTENSIONS = {'.xlsx', '.xls'}


@staff_member_required
def export(request):
    print("EXPORT")
    if request.method == 'GET':
        # content = services.full_export()
        content = services.export({"director": {"first_name": True}})
        pass
        return content
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@staff_member_required
def imp(request):
    print("IMPORT")
    if request.method == 'POST':
        file = request.FILES['userfile']
        for i in ALLOWED_EXTENSIONS:
            if file.name.endswith(i):
                services.imp(file)
                break
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@staff_member_required
def update(request):
    print("EXPORT")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
