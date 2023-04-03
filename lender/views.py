from django.shortcuts import render
from rest_framework import status, viewsets
from .models import Lender
from .serializers import LenderSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.pagination import PageNumberPagination

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