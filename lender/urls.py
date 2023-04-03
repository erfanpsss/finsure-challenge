from django.urls import path
from .views import LenderViewSet, LenderBulkImportViewSet, LenderBulkExportViewSet
from utils.constants import (
    RETRIEVE_PATCH_DELETE_ALLOWED_METHODS,
    LIST_CREATE_ALLOWED_METHODS,
    POST_ONLY_ALLOWED_METHODS,
    GET_ONLY_ALLOWED_METHODS
)



urlpatterns = [
    path(
        "import/",
        LenderBulkImportViewSet.as_view(POST_ONLY_ALLOWED_METHODS),
        name="lenders_import",
    ),   
    path(
        "export/",
        LenderBulkExportViewSet.as_view(GET_ONLY_ALLOWED_METHODS),
        name="lenders_export",
    ),   
    
    path(
        "",
        LenderViewSet.as_view(LIST_CREATE_ALLOWED_METHODS),
        name="lenders",
    ),   
    path(
        "<pk>/",
        LenderViewSet.as_view(RETRIEVE_PATCH_DELETE_ALLOWED_METHODS),
        name="lender",
    ),    
]
