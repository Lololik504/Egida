from accounts.serializers import *
from .backends import MyAuthentication

from .models import MyUser


def get_user_class(user):
    if user.permission == MyUser.Permissions.SCHOOL.value:
        try:
            return SchoolUser.objects.get(pk=user.pk)
        except:
            return None
    elif user.permission == MyUser.Permissions.DISTRICT.value:
        try:
            return DistrictUser.objects.get(pk=user.pk)
        except:
            return None
    elif user.permission == MyUser.Permissions.DEPARTAMENT.value:
        try:
            return DepartamentUser.objects.get(pk=user.pk)
        except:
            return None
    elif user.permission == MyUser.Permissions.ADMIN.value:
        try:
            return AdminUser.objects.get(pk=user.pk)
        except:
            return None


def get_user_from_request(request):
    try:
        data = request
        user_token = MyAuthentication.authenticate(MyAuthentication(), request)
        my_user = user_token[0]
        my_user = get_user_class(my_user)
        return my_user
    except:
        return None
