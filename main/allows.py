from accounts.models import SchoolUser, DistrictUser, MyUser
from main.models import Building


def school_allow(user, school):
    if user.permission > MyUser.Permissions.SCHOOL.value:
        return False
    if isinstance(user, SchoolUser):
        user_school = user.school
        if school.INN != user_school.INN:
            return False
    elif isinstance(user, DistrictUser):
        if user.district != school.district:
            return False
    else:
        return True
    return True


def building_allow(building:Building, user):
    if user.permission > MyUser.Permissions.SCHOOL.value:
        return False
    if isinstance(user, SchoolUser):
        user_school = user.school
        if building.school.INN != user_school.INN:
            return False
    elif isinstance(user, DistrictUser):
        if user.district != building.school.district:
            return False
    else:
        return True
    return True


def district_allow(user, district):
    if user.permission > MyUser.Permissions.DISTRICT.value:
        return False
    if isinstance(user, DistrictUser):
        if user.district != district:
            return False
    else:
        return True


def departament_allow(user):
    if user is None:
        return False
    if user.permission > MyUser.Permissions.DEPARTAMENT.value:
        return False
    else:
        return True
