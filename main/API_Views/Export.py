from loguru import logger
from requests import Response
from rest_framework import permissions, status
from rest_framework.utils import json
from rest_framework.views import APIView

from main.allows import departament_allow
from main.models import get_model_name
from main.serializers import PersonalAllInfoSerializer
from main.services import find_school_and_allow_user, get_director, get_bookkeeper, get_updater, get_zavhoz, export, \
    full_export


class ExportExcel(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data: dict = request.headers['data']
        if isinstance(data, str):
            data = json.loads(data)
        user = request.my_user
        if (user == None):
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data={'detail': 'You need to authorize'})
        if not (departament_allow(user)):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        if not data.__contains__("full"):
            resp = export(data)
        else:
            resp = full_export()
        # resp = full_export()
        return resp
