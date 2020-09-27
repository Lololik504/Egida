from django.shortcuts import render, HttpResponse
from .models import District, School
from .services import get_current_district, get_schools_by_district


# Create your views here.

def index(request):
    districts = District.objects.all()
    context = {'districts': districts}
    return render(request, 'main/index.html', context)


def district(request):
    url = get_current_district(request)
    districts = District.objects.all()
    require_list = list(filter((lambda f: f.url == url), districts))
    if len(require_list) == 1:
        require_dist = require_list[0]
    schools = get_schools_by_district(require_dist)
    context = {
        'district': require_dist,
        'schools': schools
    }
    return render(request, 'main/district.html', context)
