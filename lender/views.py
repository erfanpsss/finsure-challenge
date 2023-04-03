from rest_framework import status, viewsets, parsers
from .models import Lender
from .serializers import LenderSerializer, LenderBulkSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from django.shortcuts import HttpResponse
from rest_framework.pagination import PageNumberPagination
import csv

class LenderPagination(PageNumberPagination):
    page_size = 5

class LenderViewSet(viewsets.ModelViewSet):
    """
    A viewset for creating, retrieving, listing, updating, and deleting Lender records.
    """
    permission_classes = []
    serializer_class = LenderSerializer
    queryset = Lender.objects.all()
    pagination_class = LenderPagination

    @swagger_auto_schema(
        tags=["Lender"],
        request_body=LenderSerializer
    )

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "list":
            return queryset.filter(active=True)
        return queryset

    

class LenderBulkImportViewSet(viewsets.ViewSet):
    """
    A viewset for uploading lenders in bulk as csv.
    """

    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.FileUploadParser,
    )
    permission_classes = []
    serializer_class = LenderBulkSerializer

    @swagger_auto_schema(
        request_body=LenderBulkSerializer,
        responses={
            status.HTTP_200_OK: openapi.Response(
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "result": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
                examples={
                    "application/json": {
                        "result": "10 created, 0 failed, failed items: ",
                    }
                },
                description="File has been imported",
            ),
        },
        
    )
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        report = serializer.create(serializer.validated_data)
        result = (
            f"{report.get('created_count')} created, "
            f"{report.get('failed_count')} failed, "
            f"failed items: {', '.join(report.get('failed_items'))}"
        )
        return Response({"result": result})
    

class LenderBulkExportViewSet(viewsets.ViewSet):
    """
    A viewset for downloading lenders in bulk as csv.
    """

    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.FileUploadParser,
    )
    permission_classes = []
    serializer_class = LenderBulkSerializer

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: openapi.Response('File Attachment', schema=openapi.Schema(type=openapi.TYPE_FILE)),
        },
        produces='application/csv',
    )
    def retrieve(self, request, *args, **kwargs):
        lenders_data = Lender.objects.all().values()
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="lenders.csv"'},
        )
        writer = csv.writer(response)
        writer.writerow([field.name for field in Lender._meta.fields])
        for data in lenders_data:
            writer.writerow(data.values())
        return response
    
