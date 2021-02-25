from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from loguru import logger
from main.services import find_school_and_allow_user
from main.serializers.serializers import DocumentsSerializer


class DocumentsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        try:
            school = find_school_and_allow_user(INN, user)
            docs = school.document_set.get_or_create()[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        documents_serializer = DocumentsSerializer(docs)
        return Response({'documents': documents_serializer.data})

    def post(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        doc_id = data['doc-id']
        if request.FILES:
            file = request.FILES['file']
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": "File is not provided"})
        user = request.my_user
        try:
            school = find_school_and_allow_user(INN, user)
            docs = school.document_set.get_or_create()[0]

        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        if doc_id == 'passport_BTI':
            docs.passport_BTI = file
        elif doc_id == 'topographic_plan':
            docs.topographic_plan = file
        elif doc_id == 'teplosnabj_MK':
            docs.teplosnabj_MK = file
        elif doc_id == 'vodosnabj_MK':
            docs.vodosnabj_MK = file
        elif doc_id == 'electrosnabj_MK':
            docs.electrosnabj_MK = file
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": "No such doc_id"})
        docs.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        doc_id = data['doc_id']
        user = request.my_user
        try:
            school = find_school_and_allow_user(INN, user)
            docs = school.document_set.get()
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})

        if doc_id == 'passport_BTI':
            docs.passport_BTI.delete()
        elif doc_id == 'topographic_plan':
            docs.topographic_plan.delete()
        elif doc_id == 'teplosnabj_MK':
            docs.teplosnabj_MK.delete()
        elif doc_id == 'vodosnabj_MK':
            docs.vodosnabj_MK.delete()
        elif doc_id == 'electrosnabj_MK':
            docs.electrosnabj_MK.delete()
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": "No such doc_id"})
        docs.save()
        return Response(status=status.HTTP_200_OK)
