from urllib.request import Request

from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework import permissions
from rest_framework.views import APIView

from accounts.backends import MyAuthentication
from accounts.services import *
from .allows import *
from accounts import excel
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
