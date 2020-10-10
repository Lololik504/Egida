from rest_framework import status
from rest_framework.response import Response

from accounts.models import SchoolUser, DistrictUser


def school_allow(user, school):
    if isinstance(user, SchoolUser):
        user_school = user.school
        if school.INN != user_school.INN:
            return False
    elif isinstance(user, DistrictUser):
        if user.district != school.district:
            return False
    else:
        return True
