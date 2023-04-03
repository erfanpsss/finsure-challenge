from django.urls import path
from .views import LenderViewSet
from utils.constants import (
    RETRIEVE_PATCH_DELETE_ALLOWED_METHODS,
    LIST_CREATE_ALLOWED_METHODS
)



urlpatterns = [
    path(
        "lender/<pk>/",
        LenderViewSet.as_view(RETRIEVE_PATCH_DELETE_ALLOWED_METHODS),
        name="lender",
    ),    
    path(
        "lender/",
        LenderViewSet.as_view(LIST_CREATE_ALLOWED_METHODS),
        name="lenders",
    ),        
]
