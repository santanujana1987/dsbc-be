from django.shortcuts import render
from rest_framework import viewsets
from accounts.master.ledger_category_serializer import LedgerCategorySerializer
from accounts.master.ledger_group_serializer import LedgerGroupSerializer

from accounts.models import LedgerGroup
from rest_framework.permissions import IsAuthenticated # new import

# ViewSets define the view behavior.
class LedgerGroupViewSet(viewsets.ModelViewSet):
    queryset = LedgerGroup.objects.all()
    serializer_class = LedgerGroupSerializer