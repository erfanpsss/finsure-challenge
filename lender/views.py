from django.shortcuts import render
from rest_framework import viewsets, parsers
from .models import Lender
from .serializers import LenderSerializer, LenderBulkSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin
from django.shortcuts import HttpResponse
from rest_framework.pagination import PageNumberPagination
import json
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

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    

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
        request_body=LenderBulkSerializer
    )
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response("Lenders data have been imported")
    

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

    def list(self, request, *args, **kwargs):
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
    
