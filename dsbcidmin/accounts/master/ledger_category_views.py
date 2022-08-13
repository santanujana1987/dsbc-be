from django.shortcuts import render
from rest_framework import viewsets
from accounts.master.ledger_category_serializer import LedgerCategorySerializer

from accounts.models import LedgerCategory
from rest_framework.permissions import IsAuthenticated # new import

# LedgerCategory ViewSets define the view behavior.
class LedgerCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = LedgerCategory.objects.all()
    serializer_class = LedgerCategorySerializer

    
        

## LedgerCategory End
