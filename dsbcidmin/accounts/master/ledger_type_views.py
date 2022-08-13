from http.client import responses
from urllib import response
from django.shortcuts import render
from rest_framework import viewsets
from accounts.master.ledger_type_serializer import LedgerTypesSerializer
from accounts.models import LedgerTypes
from rest_framework.permissions import IsAuthenticated

# ViewSets define the view behavior.
class LedgerTypesViewSet(viewsets.ModelViewSet):
    #LedgerTypesSerializer.Meta.depth=1
    queryset = LedgerTypes.objects.all()
    serializer_class = LedgerTypesSerializer

## LedgerTypes End
