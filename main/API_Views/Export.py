from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from main.allows import departament_allow
from main.services import export, full_export


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
