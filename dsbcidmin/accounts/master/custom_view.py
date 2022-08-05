from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from accounts.views import UserSerializer

class CustomViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def afs(self, request):
        
        queryset = User.objects.all()
        serializer = UserSerializer(queryset,many=True)
