from django.shortcuts import render, redirect
from django.urls import reverse

from . import excel
from .serializers import *





def test(request):
    excel.create_new_schools_and_users_from_excel()
    return redirect(reverse('start_page'))


def index(request):
    districts = District.objects.all()
    urls = []
    for district in districts:
        urls.append(district.name)
    context = {
        'districts': districts,
        'urls': urls
    }
    return render(request, 'main/index.html', context)
