from rest_framework import permissions
from rest_framework.views import APIView


class TEST(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        pass