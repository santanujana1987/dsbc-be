from unicodedata import category, name
from rest_framework.decorators import api_view

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import permissions

from accounts.models import LedgerCategory, LedgerTypes

class AccountingCustomEndPoints(APIView):

    def get_category(self,ledger_types):
        category[ledger_types.category.id] = ledger_types.category.name
        return category
    
    @api_view(['GET'])
    @permission_classes((AllowAny, ))
    def get(self, request):
       permission_classes = (permissions.IsAuthenticatedOrReadOnly,) 
       queryset = LedgerCategory.objects.all() 
       ledger_types = LedgerTypes.objects.filter(ledger_category_id=2)
       final = {}
       categories=list( set( map(self.get_category,ledger_types) )  )
       return response.Response({'filtered_category':categories},status=status.HTTP_200_OK)


    
        

## LedgerCategory End
